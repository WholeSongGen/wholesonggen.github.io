---
layout: home
---
<head>
    <link rel="stylesheet" href="styles.css">
</head>

<!-- <hr color="#E8E8E8"> -->
<!-- <br> -->

This is the demo page of the paper under review: <i>Whole-song Hierarchical Generation of Symbolic Music Using Cascaded Diffusion Models</i>.

In the following, we first show the audible samples corresponding to the sheet music in the submitted paper. Then we show more examples of whole-song music generation.

## Audible Samples of the Sheet Music in the Submission

### Figure 2: An example of whole song generation of 40 measures.
- Generated Lead Sheet and Accompaniment. (Note: Merge two piano tracks, bpm=90)
- Generated Counterpoint(Melody reduction and chord)

### Figure 5: Examples of generated Counterpoint of "A8" phrases in Eb major.

(Note: please break the long midi file into 8-measure samples.)
- (a)-(f): These samples are only conditioned on the content of the higher-level language Form.
- (g)-(h): These samples are further conditioned on external control of chord progression latent representation. The representation fed to the model is the latent code of a sequence of Eb major chords.

### Figure 6: Examples of generated Lead Sheet of "A8" phrases in Eb major.
(Note: please note (a) is in the beginning of the midi and is different from all others. Please break the long midi file into 8-measure samples.)

All the following lead sheet is based on the higher-level language Form and the following Counterpoint (Figure 6(a)):
- (b)-(g): These samples are only conditioned on the content of the higher-level language Form and Counterpoint.
- (h)-(i): These samples are further conditioned on external control of rhythm latent representation. The representation fed to the model is the latent code of a sequence of all16-th notes.

### Figure 7: Examples of generated Accompaniment of "A8" phrases in Eb major.
(Note: please note (a) is in the beginning of the midi and is different from all others. Please break the long midi file into 8-measure samples.)

All the following lead sheet is based on the higher-level language Form, Counterpoint (Figure6(a)) and the following Lead Sheet (Figure 7(a)):
- (b)-(d): These samples are only conditioned on the content of the higher-level language Form and Counterpoint.
- (e): These samples are further conditioned on external control of texture latent representation. The representation fed to the model is the latent code of a sequence of Alberti bass texture, where left hand plays Eb quarter note and the right hand plays Alberti pattern in Eb chord.

<html>
<section id="fig2_melacc">
<midi-player src="/media/fig2_melacc.mid" sound-font visualizer="#Vis"> </midi-player>
<midi-player src="/media/tmp_nopedal.mid" sound-font visualizer="#Vis"> </midi-player>
<midi-visualizer type="piano-roll" id="Vis"> </midi-visualizer>
</section>
</html>

<script
    src="https://cdn.jsdelivr.net/combine/npm/tone@14.7.58,npm/@magenta/music@1.23.1/es6/core.js,npm/focus-visible@5,npm/html-midi-player@1.5.0"></script>

<!-- Thanks <a href="https://cifkao.github.io/html-midi-player/">html-midi-player</a> for the excellent MIDI visualization. -->

