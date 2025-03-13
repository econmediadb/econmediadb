# Using graphviz  [graphviz](https://graphviz.org)

Graphviz is open source graph visualization software. Graph visualization is a way of representing structural information as diagrams of abstract graphs and networks. It has important applications in networking, bioinformatics, software engineering, database and web design, machine learning, and in visual interfaces for other technical domains.

## Installing in Fedora 41


```bash
$ sudo dnf install graphviz
```


## Testing

```bash
$ echo 'digraph { a -> b }' | dot -Tsvg > output.svg

```