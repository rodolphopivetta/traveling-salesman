latex -interaction=nonstopmode relatorio
# bibtex relatorio
latex -interaction=nonstopmode relatorio
latex -interaction=nonstopmode relatorio
pdflatex -interaction=nonstopmode relatorio
# gs -sOutputFile=tcc_pb.pdf -sDEVICE=pdfwrite -sColorConversionStrategy=Gray -dProcessColorModel=/DeviceGray -dCompatibilityLevel=1.4 -dNOPAUSE -dBATCH tcc.pdf
