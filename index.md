---
layout: home
---
<head>
    <link rel="stylesheet" href="styles.css">
</head>


This is the demo page of the paper under review: <i>Whole-song Hierarchical Generation of Symbolic Music Using Cascaded Diffusion Models</i>. In the following, we first show the audible samples corresponding to the sheet music in the submitted paper. Then we show more examples of whole-song music generation.

<div class="dotted-box" id="def">
<div class="center-stuff">
4 levels of hierarchical musical languages are involved in the demos:
</div>
<div class="center-stuff">
<ul>
    <li><i>Form</i>: key changes and phrase division.</li>
    <li><i>Counterpoint</i>: melody reduction and simplified chord.</li>
    <li><i>Lead Sheet</i>: lead melody and chord.</li>
    <li><i>Accompaniment</i>: accompaniment (literally).</li>
</ul>
</div>
</div>

<br>
In the piano-roll visualization, <font color="#e03c34">red</font> notes indicate lead melody, and <font color="#2B7ADB">blue</font> notes indicate either chord (in *Lead Sheet*), simplified chord (in *Counterpoint*), or accompaniment (*Accompaniment*) according to the given context. 

<!-- <hr color="#E8E8E8"> -->
<br>

# Audible Samples of the Sheet Music in the Submission

### **Figure 2:** An example of whole song generation of 40 measures.

 <!-- Color Legend -->
<div class="legend">
  <div class="legend-item">
    <div class="color-box" style="background-color: #efefef;"></div>
    <span>Intro (<b>i</b>) / Outro (<b>o</b>)</span>
  </div>
  <div class="legend-item">
    <div class="color-box" style="background-color: #faf5eb;"></div>
    <span>Phrase <b>A</b></span>
  </div>
  <div class="legend-item">
    <div class="color-box" style="background-color: #faedf7;"></div>
    <span>Phrase <b>B</b></span>
  </div>
  <div class="legend-item">
    <div class="color-box" style="background-color: #ebeffa;"></div>
    <span>Bridge (<b>b</b>)</span>
  </div>
</div>

The given phrase configuration is **i**4**A**4**A**4**B**8**b**4**A**4**B**8**o**4, which stands for 4-measure intro, 4-measure phrase A, etc.

- Generated full song (lead melody and accompaniment).
<section class="vis type1">
    <midi-player src="/media/fig2_melacc.mid" sound-font visualizer="#Vis-fig2-melacc"> </midi-player>
    <midi-visualizer src="/media/fig2_melacc.mid" type="piano-roll" id="Vis-fig2-melacc"> </midi-visualizer>
    <br>
</section>
- Generated corresponding *Counterpoint*.
<section class="vis type1">
    <midi-player src="/media/fig2_cp.mid" sound-font visualizer="#Vis-fig2-cp"> </midi-player>
    <midi-visualizer src="/media/fig2_cp.mid" type="piano-roll" id="Vis-fig2-cp"> </midi-visualizer>
</section>
<br>

### **Figure 5:** Examples of generated *Counterpoint* of "A8" phrases in Eb major.

- (a)-(f): These samples are only conditioned on the content of the <a href="#def">higher-level language</a> *Form*.
<section>
    <!-- <img src="img/fig5_a.png"> -->
    <midi-player src="/media/fig5_a.mid" sound-font visualizer="#Vis-fig5-0"> </midi-player>
    <!-- <img src="img/fig5_b.png"> -->
    <midi-player src="/media/fig5_b.mid" sound-font visualizer="#Vis-fig5-0"> </midi-player>
    <!-- <img src="img/fig5_c.png"> -->
    <midi-player src="/media/fig5_c.mid" sound-font visualizer="#Vis-fig5-0"> </midi-player>
    <!-- <img src="img/fig5_d.png"> -->
    <midi-player src="/media/fig5_d.mid" sound-font visualizer="#Vis-fig5-0"> </midi-player>
    <!-- <img src="img/fig5_e.png"> -->
    <midi-player src="/media/fig5_e.mid" sound-font visualizer="#Vis-fig5-0"> </midi-player>
    <!-- <img src="img/fig5_f.png"> -->
    <midi-player src="/media/fig5_f.mid" sound-font visualizer="#Vis-fig5-0"> </midi-player>
    <midi-visualizer type="piano-roll" id="Vis-fig5-0"> </midi-visualizer>
    <br>
</section>

- (g)-(h): These samples are further conditioned on external control of chord progression latent representation. The representation fed to the model is the latent code of a sequence of Eb major chords.
<section>
    <!-- <img src="img/fig5_g.png"> -->
    <midi-player src="/media/fig5_g.mid" sound-font visualizer="#Vis-fig5-1"> </midi-player>
    <!-- <img src="img/fig5_h.png"> -->
    <midi-player src="/media/fig5_h.mid" sound-font visualizer="#Vis-fig5-1"> </midi-player>
    <midi-visualizer type="piano-roll" id="Vis-fig5-1"> </midi-visualizer>
</section>
<br>

### **Figure 6:** Examples of generated *Lead Sheet* of "A8" phrases in Eb major.

All the following samples are based on the <a href="#def">higher-level language</a> *Form* and the following *Counterpoint* (**Figure 6(a)**):
<section>
    <!-- <img src="img/fig6_a.png"> -->
    <midi-player src="/media/fig6_a.mid" sound-font visualizer="#Vis-fig6-a"> </midi-player>
    <midi-visualizer type="piano-roll" id="Vis-fig6-a"> </midi-visualizer>
    <br>
</section>

- (b)-(g): These samples are only conditioned on the content of the <a href="#def">higher-level language</a> *Form* and *Counterpoint*.
<section>
    <midi-player src="/media/fig6_b.mid" sound-font visualizer="#Vis-fig6-0"> </midi-player>
    <midi-player src="/media/fig6_c.mid" sound-font visualizer="#Vis-fig6-0"> </midi-player>
    <midi-player src="/media/fig6_d.mid" sound-font visualizer="#Vis-fig6-0"> </midi-player>
    <midi-player src="/media/fig6_e.mid" sound-font visualizer="#Vis-fig6-0"> </midi-player>
    <midi-player src="/media/fig6_f.mid" sound-font visualizer="#Vis-fig6-0"> </midi-player>
    <midi-player src="/media/fig6_g.mid" sound-font visualizer="#Vis-fig6-0"> </midi-player>
    <midi-visualizer type="piano-roll" id="Vis-fig6-0"> </midi-visualizer>
    <br>
</section>

- (h)-(i): These samples are further conditioned on external control of rhythm latent representation. The representation fed to the model is the latent code of a sequence of all16-th notes.
<section>
    <midi-player src="/media/fig6_h.mid" sound-font visualizer="#Vis-fig6-1"> </midi-player>
    <midi-player src="/media/fig6_i.mid" sound-font visualizer="#Vis-fig6-1"> </midi-player>
    <midi-visualizer type="piano-roll" id="Vis-fig6-1"> </midi-visualizer>
</section>
<br>

### **Figure 7:** Examples of generated *Accompaniment* of "A8" phrases in Eb major.

All the following samples are based on the <a href="#def">higher-level language</a> *Form*, *Counterpoint* (**Figure 6(a)**) and the following *Lead Sheet* (**Figure 7(a)**):
<section>
    <!-- <img src="img/fig7_a.png"> -->
    <midi-player src="/media/fig7_a.mid" sound-font visualizer="#Vis-fig7-a"> </midi-player>
    <midi-visualizer type="piano-roll" id="Vis-fig7-a"> </midi-visualizer>
    <br>
</section>

- (b)-(d): These samples are only conditioned on the content of the <a href="#def">higher-level language</a> *Form* and *Counterpoint*.
<section>
    <midi-player src="/media/fig7_b.mid" sound-font visualizer="#Vis-fig7-0"> </midi-player>
    <midi-player src="/media/fig7_c.mid" sound-font visualizer="#Vis-fig7-0"> </midi-player>
    <midi-player src="/media/fig7_d.mid" sound-font visualizer="#Vis-fig7-0"> </midi-player>
    <midi-visualizer type="piano-roll" id="Vis-fig7-0"> </midi-visualizer>
    <br>
</section>

- (e): This sample is further conditioned on external control of texture latent representation. The representation fed to the model is the latent code of a sequence of Alberti bass texture, where left hand plays Eb quarter note and the right hand plays Alberti pattern in Eb chord.
<section>
    <midi-player src="/media/fig7_e.mid" sound-font visualizer="#Vis-fig7-1"> </midi-player>
    <midi-visualizer type="piano-roll" id="Vis-fig7-1"> </midi-visualizer>
</section>
<br>

# More Examples of Whole-song Generation

Here are we show more whole-song generation examples (lead melody and accompaniment):

 <!-- Color Legend -->
<div class="legend">
  <div class="legend-item">
    <div class="color-box" style="background-color: #efefef;"></div>
    <span>Intro (<b>i</b>) / Outro (<b>o</b>)</span>
  </div>
  <div class="legend-item">
    <div class="color-box" style="background-color: #faf5eb;"></div>
    <span>Phrase <b>A</b></span>
  </div>
  <div class="legend-item">
    <div class="color-box" style="background-color: #faedf7;"></div>
    <span>Phrase <b>B</b></span>
  </div>
  <div class="legend-item">
    <div class="color-box" style="background-color: #ebeffa;"></div>
    <span>Bridge (<b>b</b>)</span>
  </div>
</div>

- **i**4**A**4**A**4**B**8**b**4**A**4**B**8**o**4
<section class="vis type1">
    <midi-player src="/media/more1_0.mid" sound-font visualizer="#Vis-more1_0"> </midi-player>
    <midi-visualizer src="/media/more1_0.mid" type="piano-roll" id="Vis-more1_0"> </midi-visualizer>
    <midi-player src="/media/more1_1.mid" sound-font visualizer="#Vis-more1_1"> </midi-player>
    <midi-visualizer src="/media/more1_1.mid" type="piano-roll" id="Vis-more1_1"> </midi-visualizer>
    <br>
</section>

- **A**8**B**8**A**8**B**8**B**8
<section class="vis type2">
    <midi-player src="/media/more2_0.mid" sound-font visualizer="#Vis-more2_0"> </midi-player>
    <midi-visualizer src="/media/more2_0.mid" type="piano-roll" id="Vis-more2_0"> </midi-visualizer>
    <midi-player src="/media/more2_1.mid" sound-font visualizer="#Vis-more2_1"> </midi-player>
    <midi-visualizer src="/media/more2_1.mid" type="piano-roll" id="Vis-more2_1"> </midi-visualizer>
    <br>
</section>

- **i**4**A**4**B**4**b**8**A**4**B**4**o**4
<section class="vis type3">
    <midi-player src="/media/more3_0.mid" sound-font visualizer="#Vis-more3_0"> </midi-player>
    <midi-visualizer src="/media/more3_0.mid" type="piano-roll" id="Vis-more3_0"> </midi-visualizer>
    <midi-player src="/media/more3_1.mid" sound-font visualizer="#Vis-more3_1"> </midi-player>
    <midi-visualizer src="/media/more3_1.mid" type="piano-roll" id="Vis-more3_1"> </midi-visualizer>
</section>
<br>



<script
    src="https://cdn.jsdelivr.net/combine/npm/tone@14.7.58,npm/@magenta/music@1.23.1/es6/core.js,npm/focus-visible@5,npm/html-midi-player@1.5.0"></script>

Thanks <a href="https://cifkao.github.io/html-midi-player/">html-midi-player</a> for the excellent MIDI visualization.

