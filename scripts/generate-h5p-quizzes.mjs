#!/usr/bin/env node

import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve( path.dirname( fileURLToPath( import.meta.url ) ), '..' );
const CONTENT_ROOT = path.join( ROOT, 'h5p', 'content' );

const COMMON_BEHAVIOUR = {
  enableRetry: true,
  enableSolutionsButton: true,
  enableCheckButton: true
};

const A11Y = {
  a11yCheck: 'Check the answers. The responses will be marked as correct, incorrect, or unanswered.',
  a11yShowSolution: 'Show the solution. The task will be marked with its correct solution.',
  a11yRetry: 'Retry the task. Reset all responses and start the task over again.'
};

function uuid( seed ) {
  const bytes = crypto.createHash( 'sha256' ).update( seed ).digest().subarray( 0, 16 );
  bytes[ 6 ] = ( bytes[ 6 ] & 0x0f ) | 0x40;
  bytes[ 8 ] = ( bytes[ 8 ] & 0x3f ) | 0x80;
  const hex = bytes.toString( 'hex' );
  return `${hex.slice( 0, 8 )}-${hex.slice( 8, 12 )}-${hex.slice( 12, 16 )}-${hex.slice( 16, 20 )}-${hex.slice( 20 )}`;
}

function metadata( title, contentType ) {
  return { title, license: 'CC BY-NC-SA', licenseVersion: '4.0', contentType };
}

function feedback( correct ) {
  return {
    tip: '',
    chosenFeedback: correct ? 'Yes—this is one of the correct choices.' : 'Not this one. Revisit the chapter summary and try again.',
    notChosenFeedback: ''
  };
}

function multiChoice( seed, question, choices, media ) {
  const correctCount = choices.filter( choice => choice.correct ).length;
  return {
    library: 'H5P.MultiChoice 1.16',
    subContentId: uuid( `${seed}:multiple-choice` ),
    metadata: metadata( question, 'Multiple Choice' ),
    params: {
      question: `<p>${question}</p>`,
      media: media ?? { disableImageZooming: false },
      answers: choices.map( choice => ( {
        text: `<div>${choice.text}</div>`,
        correct: choice.correct,
        tipsAndFeedback: feedback( choice.correct )
      } ) ),
      behaviour: {
        ...COMMON_BEHAVIOUR,
        singlePoint: correctCount === 1,
        randomAnswers: true,
        showSolutionsRequiresInput: true,
        autoCheck: false,
        passPercentage: 100,
        showScorePoints: true
      },
      overallFeedback: [ { from: 0, to: 100, feedback: 'You got @score of @total points.' } ],
      UI: {
        showSolutionButton: 'Show solution',
        tryAgainButton: 'Retry',
        checkAnswerButton: 'Check',
        submitAnswerButton: 'Submit',
        tipsLabel: 'Show tip',
        scoreBarLabel: 'You got :num out of :total points',
        tipAvailable: 'Tip available',
        feedbackAvailable: 'Feedback available',
        readFeedback: 'Read feedback',
        wrongAnswer: 'Wrong answer',
        correctAnswer: 'Correct answer',
        shouldCheck: 'Should have been checked',
        shouldNotCheck: 'Should not have been checked',
        noInput: 'Please answer before viewing the solution',
        ...A11Y
      }
    }
  };
}

function trueFalse( seed, question, correct, media ) {
  return {
    library: 'H5P.TrueFalse 1.8',
    subContentId: uuid( `${seed}:true-false` ),
    metadata: metadata( question, 'True/False Question' ),
    params: {
      question: `<p>${question}</p>`,
      correct: String( correct ),
      media: media ?? { disableImageZooming: false },
      behaviour: {
        ...COMMON_BEHAVIOUR,
        confirmCheckDialog: false,
        confirmRetryDialog: false,
        autoCheck: false
      },
      l10n: {
        trueText: 'True',
        falseText: 'False',
        score: 'You got @score of @total points',
        checkAnswer: 'Check',
        showSolutionButton: 'Show solution',
        tryAgain: 'Retry',
        submitAnswer: 'Submit',
        wrongAnswerMessage: 'That answer is incorrect.',
        correctAnswerMessage: 'Correct.',
        scoreBarLabel: 'You got :num out of :total points',
        ...A11Y
      }
    }
  };
}

function dragText( seed, taskDescription, textField, distractors = '' ) {
  return {
    library: 'H5P.DragText 1.10',
    subContentId: uuid( `${seed}:drag-text` ),
    metadata: metadata( taskDescription, 'Drag the Words' ),
    params: {
      taskDescription: `<p>${taskDescription}</p>`,
      textField,
      distractors,
      media: { disableImageZooming: false },
      behaviour: { ...COMMON_BEHAVIOUR, instantFeedback: false },
      overallFeedback: [ { from: 0, to: 100, feedback: 'You placed @score of @total terms correctly.' } ],
      checkAnswer: 'Check',
      submitAnswer: 'Submit',
      tryAgain: 'Retry',
      showSolution: 'Show solution',
      dropZoneIndex: 'Drop zone @index.',
      empty: 'Drop zone @index is empty.',
      contains: 'Drop zone @index contains draggable @draggable.',
      ariaDraggableIndex: '@index of @count draggables.',
      tipLabel: 'Show tip',
      correctText: 'Correct!',
      incorrectText: 'Incorrect!',
      resetDropTitle: 'Reset drop',
      resetDropDescription: 'Are you sure you want to reset this drop zone?',
      grabbed: 'Draggable is grabbed.',
      cancelledDragging: 'Cancelled dragging.',
      correctAnswer: 'Correct answer:',
      feedbackHeader: 'Feedback',
      scoreBarLabel: 'You got :num out of :total points',
      ...A11Y
    }
  };
}

function blanks( seed, prompt, lines ) {
  return {
    library: 'H5P.Blanks 1.14',
    subContentId: uuid( `${seed}:blanks` ),
    metadata: metadata( prompt, 'Fill in the Blanks' ),
    params: {
      text: `<p>${prompt}</p>`,
      questions: lines.map( line => `<p>${line}</p>` ),
      media: { disableImageZooming: false },
      behaviour: {
        ...COMMON_BEHAVIOUR,
        autoCheck: false,
        caseSensitive: false,
        showSolutionsRequiresInput: true,
        separateLines: false,
        confirmCheckDialog: false,
        confirmRetryDialog: false,
        acceptSpellingErrors: false
      },
      overallFeedback: [ { from: 0, to: 100, feedback: 'You completed @score of @total blanks correctly.' } ],
      showSolutions: 'Show solution',
      tryAgain: 'Retry',
      checkAnswer: 'Check',
      submitAnswer: 'Submit',
      notFilledOut: 'Please fill in all blanks to view the solution',
      answerIsCorrect: "':ans' is correct",
      answerIsWrong: "':ans' is wrong",
      answeredCorrectly: 'Answered correctly',
      answeredIncorrectly: 'Answered incorrectly',
      solutionLabel: 'Correct answer:',
      inputLabel: 'Blank input @num of @total',
      inputHasTipLabel: 'Tip available',
      tipLabel: 'Tip',
      scoreBarLabel: 'You got :num out of :total points',
      a11yCheckingModeHeader: 'Checking mode',
      ...A11Y
    }
  };
}

function markWords( seed, taskDescription, textField, media ) {
  return {
    library: 'H5P.MarkTheWords 1.11',
    subContentId: uuid( `${seed}:mark-words` ),
    metadata: metadata( taskDescription, 'Mark the Words' ),
    params: {
      taskDescription: `<p>${taskDescription}</p>`,
      textField,
      media: media ?? { disableImageZooming: false },
      behaviour: { ...COMMON_BEHAVIOUR, showScorePoints: true },
      overallFeedback: [ { from: 0, to: 100, feedback: 'You marked @score of @total terms correctly.' } ],
      checkAnswerButton: 'Check',
      submitAnswerButton: 'Submit',
      tryAgainButton: 'Retry',
      showSolutionButton: 'Show solution',
      correctAnswer: 'Correct!',
      incorrectAnswer: 'Incorrect!',
      missedAnswer: 'Answer not found!',
      displaySolutionDescription: 'The text now shows the solution.',
      scoreBarLabel: 'You got :num out of :total points',
      a11yFullTextLabel: 'Full readable text',
      a11yClickableTextLabel: 'Full text where words can be marked',
      a11ySolutionModeHeader: 'Solution mode',
      a11yCheckingHeader: 'Checking mode',
      ...A11Y
    }
  };
}

const IMAGE_MIME = { '.png': 'image/png', '.svg': 'image/svg+xml' };

/**
 * Intrinsic pixel size of a figure, read from the file rather than restated
 * here, so a regenerated figure cannot silently disagree with its metadata.
 */
function imageSize( file ) {
  const bytes = fs.readFileSync( file );
  if ( path.extname( file ) === '.png' ) {
    return { width: bytes.readUInt32BE( 16 ), height: bytes.readUInt32BE( 20 ) };
  }
  const viewBox = /viewBox="[\d.]+ +[\d.]+ +([\d.]+) +([\d.]+)"/.exec( bytes.toString( 'utf8', 0, 4096 ) );
  if ( !viewBox ) throw new Error( `${file}: no viewBox to take the image size from` );
  return { width: Math.round( Number( viewBox[ 1 ] ) ), height: Math.round( Number( viewBox[ 2 ] ) ) };
}

/**
 * A figure from `images/`, as the media slot of a question. The writer below
 * finds these by walking the finished questions, so naming one here is all it
 * takes to have the file copied and the H5P.Image dependency declared.
 */
function image( seed, name, alt ) {
  const mime = IMAGE_MIME[ path.extname( name ) ];
  if ( !mime ) throw new Error( `${name}: only PNG and SVG figures are supported` );
  return {
    type: {
      library: 'H5P.Image 1.1',
      subContentId: uuid( `${seed}:image:${name}` ),
      metadata: metadata( alt, 'Image' ),
      params: {
        contentName: 'Image',
        alt,
        decorative: false,
        file: { path: `images/${name}`, mime, ...imageSize( path.join( ROOT, 'images', name ) ) }
      }
    },
    disableImageZooming: false
  };
}

/** The `images/...` paths a quiz's questions refer to, in first-use order. */
function figures( quiz ) {
  const paths = new Set();
  for ( const question of quiz.questions ) {
    const media = question.params.media?.type;
    if ( media?.library.startsWith( 'H5P.Image' ) ) paths.add( media.params.file.path );
  }
  return [ ...paths ];
}

const quizzes = [
  {
    chapter: 1,
    title: 'The Need for Relativity Review',
    questions: [
      multiChoice( 'ch01', 'Why are the Michelson–Morley interferometer’s two perpendicular arms essential to the ether-wind test?', [
        { text: 'Rotating the apparatus swaps the arms’ orientation relative to the proposed ether wind, so a directional travel-time difference would change.', correct: true },
        { text: 'They force light to travel faster in one arm than in the other.', correct: false },
        { text: 'They make one beam pass through water while the other remains in air.', correct: false },
        { text: 'They remove the need to compare the phases of the returning beams.', correct: false }
      ], image( 'ch01', 'ch01-michelson-morley.svg', 'Schematic of the Michelson–Morley interferometer with perpendicular light paths, a beam splitter, mirrors, and a detector.' ) ),
      trueFalse( 'ch01', 'To first order in the water speed divided by c, relativistic velocity addition reproduces Fizeau’s partial-drag coefficient 1 − 1/n².', true ),
      dragText( 'ch01', 'Complete the contrast between Galilean kinematics and the optical null result.', 'The Galilean rule gives u′x = *ux − v*. It therefore predicts an *ether wind* for a moving laboratory, whereas Michelson–Morley found *no systematic fringe shift*. Einstein instead required every inertial observer to measure the same vacuum light speed *c*.', '*ux + v*\n*complete ether drag*' ),
      blanks( 'ch01', 'Complete the comparison between the predicted and observed Michelson–Morley signals.', [ 'For the 1887 apparatus, a stationary-ether model predicted about *0.4/.4* fringe, while rotation produced *no/zero/0* systematic fringe shift.' ] ),
      markWords( 'ch01', 'Mark the two statements that form Einstein’s postulates.', 'The *laws of physics have the same form in every inertial frame*, and the *vacuum speed of light is the same for every inertial observer*. An ether wind and absolute uniform motion are therefore not observable.' )
    ]
  },
  {
    chapter: 2,
    title: 'Special Relativity Review',
    questions: [
      multiChoice( 'ch02', 'A second event lies in the region labelled “elsewhere,” outside the origin’s light cone. How is it separated from the origin?', [
        { text: 'Spacelike: different inertial frames may reverse the event order, but no sub-light signal can connect the events.', correct: true },
        { text: 'Timelike: every inertial frame must agree that it occurs after the origin.', correct: false },
        { text: 'Lightlike: only a light signal can connect it to the origin.', correct: false },
        { text: 'Simultaneous in every inertial frame.', correct: false }
      ], image( 'ch02', 'ch02-light-cone.svg', 'Spacetime diagram showing the future and past light cones, timelike regions inside them, and spacelike regions outside them.' ) ),
      trueFalse( 'ch02', 'The proper time between two events is measured by one clock that is present at both events.', true ),
      dragText( 'ch02', 'Complete the three central transformation rules.', 'A moving clock accumulates *less* proper time, a moving object contracts *along the direction of motion*, and all inertial observers calculate the same *spacetime interval*. The separate time and space differences are *frame dependent*.', '*more*\n*in every direction*' ),
      blanks( 'ch02', 'Evaluate the Lorentz factor and length contraction at 0.8c.', [ 'At v = 0.8c, γ = *1.67/1.667*, so a moving object’s length is *0.6* of its proper length.' ] ),
      markWords( 'ch02', 'Mark the two features that every inertial observer agrees on.', 'Observers agree on the *spacetime interval* and on an event pair’s *classification as timelike, spacelike, or lightlike*; they need not agree on the separate distance, elapsed time, or simultaneity.' )
    ]
  },
  {
    chapter: 3,
    title: 'Relativistic Dynamics Review',
    questions: [
      multiChoice( 'ch03', 'For a massless particle, what happens to the energy–momentum triangle shown above?', [
        { text: 'The rest-energy leg becomes zero, so the relation reduces to E = pc.', correct: true },
        { text: 'The momentum leg becomes zero, so the relation reduces to E = mc².', correct: false },
        { text: 'All three sides remain nonzero and equal.', correct: false },
        { text: 'The total-energy side becomes zero while momentum remains nonzero.', correct: false }
      ], image( 'ch03', 'ch03-energy-momentum.svg', 'Right triangle with legs pc and mc squared and hypotenuse E, illustrating the invariant energy–momentum relation.' ) ),
      trueFalse( 'ch03', 'For the same total beam energy, a fixed-target experiment makes as much center-of-momentum energy available for new particles as a head-on collider.', false ),
      dragText( 'ch03', 'Complete the relativistic momentum and energy relations.', 'A massive particle has momentum p = *γmu*, kinetic energy K = *(γ − 1)mc²*, and total energy E = *γmc²*. A massless photon obeys E = *pc*.', '*mu*\n*mc²*' ),
      blanks( 'ch03', 'Evaluate the energy of a particle moving at 0.6c.', [ 'At u = 0.6c, γ = *1.25*, so the kinetic energy is *0.25* mc².' ] ),
      markWords( 'ch03', 'Mark the frame and system property used most directly in a threshold calculation.', 'In the *center-of-momentum frame* the total momentum is zero, and the system’s *invariant mass* determines which final-state rest masses can be created.' )
    ]
  },
];

const dependencies = [
  [ 'H5P.QuestionSet', 1, 21 ],
  [ 'H5P.MultiChoice', 1, 16 ],
  [ 'H5P.TrueFalse', 1, 8 ],
  [ 'H5P.DragText', 1, 10 ],
  [ 'H5P.Blanks', 1, 14 ],
  [ 'H5P.MarkTheWords', 1, 11 ]
];

function dependency( [ machineName, majorVersion, minorVersion ] ) {
  return { machineName, majorVersion, minorVersion };
}

function questionSet( quiz ) {
  return {
    progressType: 'dots',
    passPercentage: 80,
    questions: quiz.questions,
    introPage: {
      showIntroPage: false,
      title: quiz.title,
      introduction: '<p>Five short questions review the chapter.</p>',
      startButtonText: 'Start review'
    },
    texts: {
      prevButton: 'Previous question',
      previous: 'Previous',
      nextButton: 'Next question',
      next: 'Next',
      finishButton: 'Finish',
      submitButton: 'Submit',
      textualProgress: 'Question @current of @total',
      jumpToQuestion: 'Question %d of %total',
      questionLabel: 'Question',
      readSpeakerProgress: 'Question @current of @total',
      unansweredText: 'Unanswered',
      answeredText: 'Answered',
      currentQuestionText: 'Current question',
      navigationLabel: 'Questions',
      questionSetInstruction: 'Choose a question to display'
    },
    disableBackwardsNavigation: false,
    randomQuestions: false,
    endGame: {
      showResultPage: true,
      showSolutionButton: true,
      showRetryButton: true,
      noResultMessage: 'Finished',
      message: 'Chapter review complete',
      amountCorrect: '@finals of @totals correct',
      scoreBarLabel: 'You got @finals out of @totals points',
      scoreHeader: 'Score',
      overallFeedback: [ { from: 0, to: 100, feedback: 'You earned @score of @total points.' } ],
      solutionButtonText: 'Show solutions',
      retryButtonText: 'Retry',
      finishButtonText: 'Finish',
      submitButtonText: 'Submit',
      showAnimations: false,
      skippable: false,
      skipButtonText: 'Skip video'
    },
    override: {
      checkButton: true,
      showSolutionButton: 'on',
      retryButton: 'on'
    }
  };
}

for ( const quiz of quizzes ) {
  const chapter = String( quiz.chapter ).padStart( 2, '0' );
  const id = `ch${chapter}-chapter-review`;
  const root = path.join( CONTENT_ROOT, id );
  const content = path.join( root, 'content' );
  fs.mkdirSync( content, { recursive: true } );

  const preloadedDependencies = dependencies.map( dependency );
  const quizFigures = figures( quiz );
  if ( quizFigures.length > 0 ) preloadedDependencies.push( dependency( [ 'H5P.Image', 1, 1 ] ) );

  const manifest = {
    title: quiz.title,
    language: 'en',
    mainLibrary: 'H5P.QuestionSet',
    embedTypes: [ 'iframe' ],
    license: 'CC BY-NC-SA',
    licenseVersion: '4.0',
    preloadedDependencies
  };

  fs.writeFileSync( path.join( root, 'h5p.json' ), `${JSON.stringify( manifest, null, 2 )}\n` );
  fs.writeFileSync( path.join( content, 'content.json' ), `${JSON.stringify( questionSet( quiz ), null, 2 )}\n` );

  for ( const figure of quizFigures ) {
    const destination = path.join( content, figure );
    fs.mkdirSync( path.dirname( destination ), { recursive: true } );
    fs.copyFileSync( path.join( ROOT, figure ), destination );
  }
}

console.log( `Generated ${quizzes.length} H5P chapter reviews (${quizzes.reduce( ( total, quiz ) => total + quiz.questions.length, 0 )} questions).` );
