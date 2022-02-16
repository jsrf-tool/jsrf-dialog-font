# JSRF Dialog Font

<div align="center">
<h1>
<span>
<img alt="source font texture" title="source font texture" src="jsrf-alphanumeric.png" height="150px"/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:arrow_right:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img alt="typeface pangram preview" title="typeface pangram preview" src="https://user-images.githubusercontent.com/99629389/154042887-4247e733-753e-49ff-ad5a-79423d2eddbd.png" width="500px">
</span>
</h1>
</div>
<br/>

## Building

### Dependencies
* python-pillow &mdash; python image manipulation library
* potrace &mdash; raster to vector autotracer
* fontforge (including python module) &mdash; general purpose font creation suite 
* GNU Make

On Arch, these can be easily installed via `pacman`:
* `pacman --sync --refresh make potrace fontforge python-pillow`

### Pipeline

Data processing pipeline as executed by the `Makefile` to convert the font spritesheet to a vector typeface:
```mermaid
graph LR;
    A(source font raster<br/>spritesheet)-->|unsprite.py<br/><pre>python-pillow</pre>|B("individual .bmp's of<br/>each sprite glyph<br/><i>(bmp/*)</i>");
    B-->|potrace-svg.sh<br/><pre>potrace</pre>|C("autotraced .svg's<br/>of indiviual glyphs<br/><i>(svg/*)</i>");
    C-->|svg2ttf.py<br/><pre>fontforge</pre>|D("vector typeface<br/>from .svg's<br/><i>(.ttf, .woff, .woff2)</i>");
```

