.PHONY: all counts plots jpeg clean

all: counts plots jpeg

counts:
	mkdir -p counts
	doit counts

plots:
	mkdir -p plots
	doit plots

jpeg:
	cd plots; mogrify -negate -rotate 90 -crop 487x635+58+96 -format jpeg *.png

clean:
	rm -rf counts
	rm -rf plots
