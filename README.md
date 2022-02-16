# JSRF Dialog Font
Generate vector typeface formats from extracted textures of the JSRF standard dialog font raster.

The combined and editted in-game source texture is:

![font source texture](media/jsrf-font-accents.png)

and after autotracing each glyph sprite and compiling into a typeface, any arbitrary text can be rendered in this typeface:

![typeface pangram preview](https://user-images.githubusercontent.com/99629389/154042887-4247e733-753e-49ff-ad5a-79423d2eddbd.png)

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
    C-->|svg2ttf.py<br/><pre>fontforge</pre>|D("vector typeface<br/>from .svg's<br/><i>(.ttf,.woff.woff2)</i>");
```

