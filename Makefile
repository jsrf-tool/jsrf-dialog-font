SHELL := /bin/bash

SOURCE_SPRITESHEET := jsrf-alphanumeric.png
TARGET := jsrf

# .PHONY: svg

BMPS = $(wildcard ./bmp/%)
SVGS = $(wildcard ./svg/%)
FONTS = $(wildcard $(TARGET).%)

all: font

font: svg $(SVGS) svg2ttf.py
	./svg2ttf.py 2>/dev/null

svg: potrace-svg.sh bmp $(BMPS)
	rm -rf ./svg/*
	mkdir -p ./svg
	cd svg ; bash -c "../potrace-svg.sh ../bmp/*.bmp ; mv -v ../bmp/*.svg ."

bmp: unsprite.py $(SOURCE_SPRITESHEET)
	./unsprite.py

clean:
	rm -rfv ./svg ||:
	rm -rfv ./bmp ||:
	rm -v $(TARGET).* ||:
