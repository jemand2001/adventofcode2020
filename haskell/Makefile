SOURCE = Day_1 Day_2

all: $(SOURCE)

%: %.hs
	ghc -o $@ $<

sorta-clean:
	rm -f *.hi *.o

clean:
	rm -f *.hi *.o
	find -name "Day_*" -executable -delete
