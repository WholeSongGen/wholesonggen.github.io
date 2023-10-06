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

- Generated Lead Sheet and Accompaniment.
<section id="fig2">
    <midi-player src="/media/fig2_melacc.mid" sound-font visualizer="#Vis-fig2-melacc"> </midi-player>
    <midi-visualizer src="/media/fig2_melacc.mid" type="piano-roll" id="Vis-fig2-melacc"> </midi-visualizer>
</section>
- Generated Counterpoint(Melody reduction and chord)
<section id="fig2">
    <midi-player src="/media/fig2_cp.mid" sound-font visualizer="#Vis-fig2-cp"> </midi-player>
    <midi-visualizer src="/media/fig2_cp.mid" type="piano-roll" id="Vis-fig2-cp"> </midi-visualizer>
</section>
<br>

### Figure 5: Examples of generated Counterpoint of "A8" phrases in Eb major.

- (a)-(f): These samples are only conditioned on the content of the higher-level language Form.
<section id="fig5">
    <midi-player src="/media/fig5_a.mid" sound-font visualizer="#Vis-fig5-0"> </midi-player>
    <midi-player src="/media/fig5_b.mid" sound-font visualizer="#Vis-fig5-0"> </midi-player>
    <midi-player src="/media/fig5_c.mid" sound-font visualizer="#Vis-fig5-0"> </midi-player>
    <midi-player src="/media/fig5_d.mid" sound-font visualizer="#Vis-fig5-0"> </midi-player>
    <midi-player src="/media/fig5_e.mid" sound-font visualizer="#Vis-fig5-0"> </midi-player>
    <midi-player src="/media/fig5_f.mid" sound-font visualizer="#Vis-fig5-0"> </midi-player>
    <midi-visualizer type="piano-roll" id="Vis-fig5-0"> </midi-visualizer>
</section>

- (g)-(h): These samples are further conditioned on external control of chord progression latent representation. The representation fed to the model is the latent code of a sequence of Eb major chords.
<section id="fig5">
    <midi-player src="/media/fig5_g.mid" sound-font visualizer="#Vis-fig5-1"> </midi-player>
    <midi-player src="/media/fig5_h.mid" sound-font visualizer="#Vis-fig5-1"> </midi-player>
    <midi-visualizer type="piano-roll" id="Vis-fig5-1"> </midi-visualizer>
</section>
<br>

### Figure 6: Examples of generated Lead Sheet of "A8" phrases in Eb major.

All the following lead sheet is based on the higher-level language Form and the following Counterpoint (Figure 6(a)):
<section id="fig6">
    <midi-player src="/media/fig6_a.mid" sound-font visualizer="#Vis-fig6-a"> </midi-player>
    <midi-visualizer src="/media/fig6_a.mid" type="piano-roll" id="Vis-fig6-a"> </midi-visualizer>
</section>

- (b)-(g): These samples are only conditioned on the content of the higher-level language Form and Counterpoint.
<section id="fig6">
    <midi-player src="/media/fig6_b.mid" sound-font visualizer="#Vis-fig6-0"> </midi-player>
    <midi-player src="/media/fig6_c.mid" sound-font visualizer="#Vis-fig6-0"> </midi-player>
    <midi-player src="/media/fig6_d.mid" sound-font visualizer="#Vis-fig6-0"> </midi-player>
    <midi-player src="/media/fig6_e.mid" sound-font visualizer="#Vis-fig6-0"> </midi-player>
    <midi-player src="/media/fig6_f.mid" sound-font visualizer="#Vis-fig6-0"> </midi-player>
    <midi-player src="/media/fig6_g.mid" sound-font visualizer="#Vis-fig6-0"> </midi-player>
    <midi-visualizer type="piano-roll" id="Vis-fig6-0"> </midi-visualizer>
</section>

- (h)-(i): These samples are further conditioned on external control of rhythm latent representation. The representation fed to the model is the latent code of a sequence of all16-th notes.
<section id="fig6">
    <midi-player src="/media/fig6_h.mid" sound-font visualizer="#Vis-fig6-1"> </midi-player>
    <midi-player src="/media/fig6_i.mid" sound-font visualizer="#Vis-fig6-1"> </midi-player>
    <midi-visualizer type="piano-roll" id="Vis-fig6-1"> </midi-visualizer>
</section>
<br>

### Figure 7: Examples of generated Accompaniment of "A8" phrases in Eb major.

All the following lead sheet is based on the higher-level language Form, Counterpoint (Figure6(a)) and the following Lead Sheet (Figure 7(a)):
<section>
    <midi-player src="/media/fig7_a.mid" sound-font visualizer="#Vis-fig7-a"> </midi-player>
    <midi-visualizer src="/media/fig7_a.mid" type="piano-roll" id="Vis-fig7-a"> </midi-visualizer>
</section>

- (b)-(d): These samples are only conditioned on the content of the higher-level language Form and Counterpoint.
<section id="fig7">
    <midi-player src="/media/fig7_b.mid" sound-font visualizer="#Vis-fig7-0"> </midi-player>
    <midi-player src="/media/fig7_c.mid" sound-font visualizer="#Vis-fig7-0"> </midi-player>
    <midi-player src="/media/fig7_d.mid" sound-font visualizer="#Vis-fig7-0"> </midi-player>
    <midi-visualizer type="piano-roll" id="Vis-fig7-0"> </midi-visualizer>
</section>

- (e): These samples are further conditioned on external control of texture latent representation. The representation fed to the model is the latent code of a sequence of Alberti bass texture, where left hand plays Eb quarter note and the right hand plays Alberti pattern in Eb chord.
<section id="fig7">
    <midi-player src="/media/fig7_e.mid" sound-font visualizer="#Vis-fig7-1"> </midi-player>
    <midi-visualizer type="piano-roll" id="Vis-fig7-1"> </midi-visualizer>
</section>

## More Examples

Here are we show more generation examples:

- i4A4A4B8b4A4B8o4
- A8B8A8B8B8
- i4A4B4b8A4B4o4
(Note: please truncate at 32 measures)

(Below: Omitted for now)


<script
    src="https://cdn.jsdelivr.net/combine/npm/tone@14.7.58,npm/@magenta/music@1.23.1/es6/core.js,npm/focus-visible@5,npm/html-midi-player@1.5.0"></script>

<!-- Thanks <a href="https://cifkao.github.io/html-midi-player/">html-midi-player</a> for the excellent MIDI visualization. -->

