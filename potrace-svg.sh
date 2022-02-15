#!/usr/bin/env bash
potrace_opts=(
  --svg
  --turdsize 0        # - suppress speckles of up to this size (default 2)
  --alphamax 0.1        # - corner threshold parameter (default 1)
  --opttolerance 1   # - curve optimization tolerance (default 0.2)
  --flat  # - whole image as a single path
  # --longcurve    # - turn off curve optimization
  # --pagesize 5mmx5mm
  --width 21mm  # - width of output image
  # --height 5mm  # - width of output image
  # -H 50in   # - height of output image
  # --resolution <n>[x<n>] - resolution (in dpi) (dimension-based backends)
  # --scale 200  # scaling factor (pixel-based backends)
  # --stretch           # - yresolution/xresolution
  # --rotate <angle>       - rotate counterclockwise by angle
  # --margin 10in
  --leftmargin 6.5mm      #  34 - 21 = 13 -> 13/2 => 6.5
  --rightmargin 6.5mm     #  34 - 21 = 13 -> 13/2 => 6.5
  # --rightmargin <dim>    - right margin
  # --topmargin <dim>      - top margin
  # --bottommargin <dim>   - bottom margin
  # --color '#ffffff'  # set foreground color (default black)
  # --fillcolor '#ff0000' # set fill color (default transparent)
  # --tight            # remove whitespace around the input image
  # --opaque           # make white shapes opaque
  --group                    #- group related paths together
)

potrace_cmd="potrace ${potrace_opts[@]} -- $@"
echo "$potrace_cmd"
exec $potrace_cmd