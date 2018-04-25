# plantUML Depth Renderer

### Setup

You'll need to layout your plantUML file such that tabs are only used to signify
objects that are optional, e.g. `alt->else->end` blocks. Then use expandtab (if using vim) for everything else

### Prerequisites

- [plantUML](http://plantuml.com/)

### Example Usage

`./renderToDepth example.puml -d 2`

this will display your UML diagram with any depth greater than 2 excluded

### Tool Help

```
$ ./renderToDepth.py -h
usage: renderToDepth.py [-h] [-d DEPTH] file

positional arguments:
  file                  UML file name

optional arguments:
  -h, --help            show this help message and exit
  -d DEPTH, --depth DEPTH
                        Anything after this depth will not be rendered
```
