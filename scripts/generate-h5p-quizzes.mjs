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
  {
    chapter: 4,
    title: 'Interference of Light Review',
    questions: [
      multiChoice( 'ch04', 'If the slit separation d increases while the wavelength and screen distance stay fixed, what happens to the double-slit fringe spacing?', [
        { text: 'It decreases because the spacing is proportional to 1/d.', correct: true },
        { text: 'It increases because the spacing is proportional to d.', correct: false },
        { text: 'It stays unchanged because only wavelength controls the pattern.', correct: false },
        { text: 'The bright and dark fringes exchange positions without changing spacing.', correct: false }
      ], image( 'ch04', 'ch04-two-slit-intensity.svg', 'Double-slit intensity pattern with regularly spaced bright fringes.' ) ),
      trueFalse( 'ch04', 'Reflection from a boundary leading into a higher-index medium adds a phase change of π.', true ),
      dragText( 'ch04', 'Complete the interference conditions.', 'A path difference Δr produces phase difference *2πΔr/λ*. Constructive interference occurs at *Δr = mλ*, while destructive interference occurs at *Δr = (m + 1/2)λ*. Stable fringes require *coherence*.', '*Δr = λ/m*\n*incoherence*' ),
      blanks( 'ch04', 'Complete the path-to-phase and fringe-spacing results.', [ 'A path difference of λ/2 gives a phase difference of *π/pi* radians, and doubling d makes the fringe spacing *half/one half/1/2* as large.' ] ),
      markWords( 'ch04', 'Mark the two statements that explain coherence and energy conservation in interference.', 'A stable pattern requires a *phase difference that remains predictable during observation*. Interference *redistributes energy between bright and dark regions*; it does not create energy.' )
    ]
  },
  {
    chapter: 5,
    title: 'Diffraction of Light Review',
    questions: [
      multiChoice( 'ch05', 'What change makes a single-slit diffraction pattern wider?', [
        { text: 'Narrowing the slit.', correct: true },
        { text: 'Widening the slit.', correct: false },
        { text: 'Increasing the screen distance while measuring angles.', correct: false },
        { text: 'Adding more illuminated grating lines without changing the slit.', correct: false }
      ], image( 'ch05', 'ch05-single-slit-intensity.svg', 'Single-slit diffraction intensity pattern with a broad central maximum and weaker side lobes.' ) ),
      trueFalse( 'ch05', 'The value m = 0 is a single-slit diffraction minimum.', false ),
      dragText( 'ch05', 'Complete the principal diffraction relations.', 'Single-slit minima obey *a sin θ = mλ*. A grating’s resolving power is *R = mN*. A circular aperture has Rayleigh angle *1.22λ/D*. Crystal planes satisfy *nλ = 2d sin θ*.', '*d sin θ = mλ*\n*λ/D²*' ),
      blanks( 'ch05', 'Complete the grating and aperture results.', [ 'A grating used in order m = 2 with N = 500 illuminated lines has resolving power *1000*, while doubling a circular aperture’s diameter makes its diffraction-limited angle *half/one half/1/2* as large.' ] ),
      markWords( 'ch05', 'Mark the two changes that improve diffraction-limited resolution.', 'A grating resolves closer wavelengths by using *more illuminated lines*. A circular instrument resolves closer angular sources by using a *larger aperture diameter*. Narrowing an ordinary slit broadens its pattern.' )
    ]
  },
  {
    chapter: 6,
    title: 'Particle Properties of Waves Review',
    questions: [
      multiChoice( 'ch06', 'Which observation most directly shows that photoelectric energy arrives in quanta?', [
        { text: 'Below a threshold frequency no electrons are emitted, regardless of intensity.', correct: true },
        { text: 'Brighter light always gives each emitted electron more kinetic energy.', correct: false },
        { text: 'All wavelengths eject electrons if the exposure lasts long enough.', correct: false },
        { text: 'The stopping potential depends only on the illuminated area.', correct: false }
      ] ),
      trueFalse( 'ch06', 'At fixed frequency above threshold, increasing light intensity raises the maximum kinetic energy of photoelectrons.', false ),
      dragText( 'ch06', 'Complete the photon relations.', 'A photon has energy *E = hf* and momentum *p = h/λ*. Photoemission obeys *Kmax = hf − φ*. In Compton scattering, a photon that loses energy has a *longer wavelength*.', '*E = h/f*\n*shorter wavelength*' ),
      blanks( 'ch06', 'Complete the pair-production and thermal-radiation results.', [ 'The rest-energy threshold for electron–positron pair production is *1.022* MeV, and total blackbody power per area scales as temperature to the power *4/four*.' ] ),
      markWords( 'ch06', 'Mark the two observations that support the photon model.', 'The photoelectric effect has a *sharp threshold frequency*, and Compton scattering shows an *angle-dependent wavelength shift*. Classical intensity alone does not explain either result.' )
    ]
  },
  {
    chapter: 7,
    title: 'Wave Properties of Particles Review',
    questions: [
      multiChoice( 'ch07', 'How does doubling a particle’s momentum change its de Broglie wavelength?', [
        { text: 'It halves the wavelength.', correct: true },
        { text: 'It doubles the wavelength.', correct: false },
        { text: 'It quadruples the wavelength.', correct: false },
        { text: 'It leaves the wavelength unchanged.', correct: false }
      ], image( 'ch07', 'ch07-two-frequency-envelope.svg', 'Two nearby matter-wave components and the envelope produced by their superposition.' ) ),
      trueFalse( 'ch07', 'For a free nonrelativistic particle, the group velocity of its wave packet equals the particle speed.', true ),
      dragText( 'ch07', 'Complete the matter-wave relationships.', 'Matter wavelength is *λ = h/p*. A localized particle requires a *wave packet*. Its envelope moves at the *group velocity*, while its individual crests move at the *phase velocity*.', '*λ = p/h*\n*single plane wave*' ),
      blanks( 'ch07', 'Complete the wavelength and uncertainty comparisons.', [ 'Doubling momentum makes λ *half/one half/1/2* as large; narrowing Δx requires the momentum spread Δp to become *larger/broader/greater*.' ] ),
      markWords( 'ch07', 'Mark the two experimental signatures of matter waves.', 'Electrons produce *crystal diffraction peaks* and individual particles build up a *two-path interference pattern*. A localized detector click is the particle-like part of the same experiment.' )
    ]
  },
  {
    chapter: 8,
    title: 'The Schrödinger Equation Review',
    questions: [
      multiChoice( 'ch08', 'Why is the infinite-well ground-state energy not zero?', [
        { text: 'A zero-momentum state cannot satisfy confinement and the well’s boundary conditions.', correct: true },
        { text: 'The potential energy inside the well is infinite.', correct: false },
        { text: 'The particle must move at the speed of light.', correct: false },
        { text: 'The wave function is required to be constant everywhere.', correct: false }
      ], image( 'ch08', 'ch08-box-modes.svg', 'The first few standing-wave modes in a one-dimensional infinite square well.' ) ),
      trueFalse( 'ch08', 'A stationary state has a time-independent probability density even though its wave function carries a time-dependent phase.', true ),
      dragText( 'ch08', 'Complete the interpretation of the wave function.', 'The quantity |Ψ|² is the *probability density*. A physical wave function must be *normalizable*. Bound-state energies arise from *boundary conditions*. Tunneling occurs because Ψ has *nonzero amplitude beyond a finite barrier*.', '*probability amplitude squared only after measurement*\n*zero amplitude inside every barrier*' ),
      blanks( 'ch08', 'Complete the infinite-well scaling.', [ 'For a one-dimensional infinite well, En is proportional to n raised to the power *2/two*, so E2/E1 = *4/four*.' ] ),
      markWords( 'ch08', 'Mark the two statements that make tunneling possible.', 'A finite barrier permits an *evanescent wave inside the classically forbidden region* and the wave function can retain *nonzero amplitude on the far side*. The particle does not need energy greater than the barrier.' )
    ]
  },
  {
    chapter: 9,
    title: 'Quantum Mechanics in Three Dimensions Review',
    questions: [
      multiChoice( 'ch09', 'For orbital angular-momentum quantum number ℓ, how many values may mℓ take?', [
        { text: '2ℓ + 1, from −ℓ through +ℓ.', correct: true },
        { text: 'ℓ, from 0 through ℓ − 1.', correct: false },
        { text: '2ℓ, excluding zero.', correct: false },
        { text: 'Only one value, mℓ = ℓ.', correct: false }
      ] ),
      trueFalse( 'ch09', 'The centrifugal barrier in the radial Schrödinger equation vanishes for ℓ = 0.', true ),
      dragText( 'ch09', 'Complete the central-potential description.', 'A central potential depends only on *r*. Its wave function separates into *radial and angular parts*. The universal angular functions are *spherical harmonics*. The barrier term is proportional to *ℓ(ℓ + 1)/r²*.', '*θ only*\n*Cartesian plane waves*' ),
      blanks( 'ch09', 'Complete the angular-momentum and oscillator counts.', [ 'For ℓ = 2 there are *5/five* allowed mℓ values; oscillator triples with the same sum nx + ny + nz have the *same/equal* energy.' ] ),
      markWords( 'ch09', 'Mark the pair of orbital-angular-momentum quantities that can be sharp simultaneously.', 'A central-potential state may have sharp *L²* and *Lz*. The noncommuting Cartesian components Lx and Ly cannot all be sharp at the same time.' )
    ]
  },
  {
    chapter: 10,
    title: 'The Hydrogen Atom Review',
    questions: [
      multiChoice( 'ch10', 'Which orbital selection rule governs an ordinary electric-dipole transition?', [
        { text: 'Δℓ = ±1.', correct: true },
        { text: 'Δℓ = 0 only.', correct: false },
        { text: 'Δn = 0 only.', correct: false },
        { text: 'Δms = ±1 is required.', correct: false }
      ], image( 'ch10', 'ch10-energy-levels.svg', 'Hydrogen energy levels and the Lyman, Balmer, and Paschen transition series.' ) ),
      trueFalse( 'ch10', 'The hydrogen ground state has orbital angular momentum ℏ, as in the original Bohr model.', false ),
      dragText( 'ch10', 'Complete the hydrogen quantum-number rules.', 'For a given n, ℓ runs from *0 to n − 1*. For a given ℓ, mℓ runs from *−ℓ to +ℓ*. The spin projection is *ms = ±1/2*. Electric-dipole transitions require *Δℓ = ±1*.', '*1 to n*\n*Δℓ = 0*' ),
      blanks( 'ch10', 'Complete the hydrogenic scaling at fixed n.', [ 'Increasing nuclear charge from Z = 1 to Z = 2 makes the binding-energy magnitude *4/four* times as large and the characteristic orbital radius *half/one half/1/2* as large.' ] ),
      markWords( 'ch10', 'Mark the two results revealed by the Stern–Gerlach experiment.', 'The beam separates into *two discrete deflections*, revealing an intrinsic *spin-one-half degree of freedom*. It does not produce a continuous range of orientations.' )
    ]
  },
  {
    chapter: 11,
    title: 'Many-Electron Atoms Review',
    questions: [
      multiChoice( 'ch11', 'What does screening do to the nuclear attraction felt by an outer electron?', [
        { text: 'It reduces the effective nuclear charge felt by the electron.', correct: true },
        { text: 'It reverses the nuclear force and makes it repulsive.', correct: false },
        { text: 'It removes all dependence on orbital penetration.', correct: false },
        { text: 'It forces every subshell with the same n to remain degenerate.', correct: false }
      ], image( 'ch11', 'ch11-ionization-energy.svg', 'First ionization energy plotted across the periodic table, showing periodic trends.' ) ),
      trueFalse( 'ch11', 'Two electrons in one spatial orbital may have the same spin projection.', false ),
      dragText( 'ch11', 'Complete the rules for many-electron atoms.', 'The *Pauli exclusion principle* limits an orbital to two opposite-spin electrons. The *Aufbau principle* fills lower-energy subshells first. *Hund’s rule* maximizes spin in degenerate orbitals. Screening produces an *effective nuclear charge*.', '*uncertainty principle*\n*bare nuclear charge for every electron*' ),
      blanks( 'ch11', 'Complete the shell and laser statements.', [ 'A K-shell vacancy lies in the shell with n = *1/one*, and laser amplification requires a population *inversion*.' ] ),
      markWords( 'ch11', 'Mark the two general trends across a period.', 'Across a period, first ionization energy generally *increases* while atomic radius generally *decreases*, as effective nuclear charge grows.' )
    ]
  },
  {
    chapter: 12,
    title: 'Molecular Structure Review',
    questions: [
      multiChoice( 'ch12', 'Why is molecular oxygen paramagnetic in the molecular-orbital description?', [
        { text: 'It has two unpaired electrons in antibonding π orbitals.', correct: true },
        { text: 'All of its electrons are paired in bonding orbitals.', correct: false },
        { text: 'Its bond order is zero.', correct: false },
        { text: 'It has six bonding regions around a central atom.', correct: false }
      ], image( 'ch12', 'ch12-mo-diagram-n2-o2.svg', 'Molecular-orbital energy-level diagrams for nitrogen and oxygen.' ) ),
      trueFalse( 'ch12', 'A molecular-orbital bond order of zero predicts a stably bound molecule in that configuration.', false ),
      dragText( 'ch12', 'Complete the molecular descriptions.', 'A bond order is half the difference between *bonding and antibonding electron counts*. Six bonding regions with no lone pairs give *octahedral* geometry. Vibrational spectra are mainly *infrared*, while rotational spectra are mainly *microwave*.', '*tetrahedral*\n*ultraviolet only*' ),
      blanks( 'ch12', 'Complete the bond-order and geometry results.', [ 'If a molecule has 8 bonding and 4 antibonding electrons, its bond order is *2/two*; six electron regions with no lone pairs form an *octahedral* geometry.' ] ),
      markWords( 'ch12', 'Mark the two intermolecular-force statements.', 'London dispersion acts between *all atoms and molecules*, while especially strong hydrogen bonding requires hydrogen bonded to *nitrogen, oxygen, or fluorine*.' )
    ]
  },
  {
    chapter: 13,
    title: 'Nuclear Physics Review',
    questions: [
      multiChoice( 'ch13', 'Why can both fusion of light nuclei and fission of heavy nuclei release energy?', [
        { text: 'Both move the products toward higher binding energy per nucleon near iron and nickel.', correct: true },
        { text: 'Both convert every nucleon entirely into radiation.', correct: false },
        { text: 'Both eliminate the strong nuclear interaction.', correct: false },
        { text: 'Both always increase the total rest mass of the products.', correct: false }
      ], image( 'ch13', 'ch13-binding-energy-curve.svg', 'Binding energy per nucleon versus mass number, peaking near iron and nickel.' ) ),
      trueFalse( 'ch13', 'A radioactive nucleus becomes more likely to decay merely because it has survived for a long time.', false ),
      dragText( 'ch13', 'Complete the nuclear-decay descriptions.', 'Alpha decay proceeds by *quantum tunneling*. Beta decay uses the *weak interaction*. Gamma decay changes nuclear *energy without changing A or Z*. Radioactive populations follow an *exponential law*.', '*electromagnetic tunneling of electrons*\n*linear law*' ),
      blanks( 'ch13', 'Complete the nuclear-size and decay relations.', [ 'Nuclear radius scales as A raised to the power *0.333/one third*, and the half-life equals ln 2 divided by the decay *constant/lambda/λ*.' ] ),
      markWords( 'ch13', 'Mark the two processes that move nuclei toward the binding-energy peak.', 'Energy can be released by *fusion of light nuclei* and by *fission of very heavy nuclei*. Both produce more tightly bound products.' )
    ]
  },
  {
    chapter: 14,
    title: 'Elementary Particles and the Standard Model Review',
    questions: [
      multiChoice( 'ch14', 'Which Standard Model interaction is carried by gluons?', [
        { text: 'The strong interaction.', correct: true },
        { text: 'The electromagnetic interaction.', correct: false },
        { text: 'The weak interaction.', correct: false },
        { text: 'Gravity.', correct: false }
      ], image( 'ch14', 'ch14-standard-model-chart.svg', 'Chart of Standard Model matter particles and force-carrying bosons.' ) ),
      trueFalse( 'ch14', 'A meson is made from three quarks, while a baryon is a quark–antiquark pair.', false ),
      dragText( 'ch14', 'Complete the Standard Model classifications.', 'Matter particles with half-integer spin are *fermions*. Force carriers are *bosons*. Three-quark hadrons are *baryons*. Quark–antiquark hadrons are *mesons*.', '*leptons only*\n*gauge fermions*' ),
      blanks( 'ch14', 'Complete the proton and detector statements.', [ 'A proton has quark content *uud*, and missing transverse momentum can signal an unseen *neutrino*.' ] ),
      markWords( 'ch14', 'Mark the two quantities that must balance in every allowed particle reaction.', 'Every reaction must conserve *electric charge* and *baryon number*. Lepton number is also conserved to excellent approximation in Standard Model reactions.' )
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
