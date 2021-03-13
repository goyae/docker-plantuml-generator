# docker-plantuml-generator

## Use Command

```
make plant
```

Convert the `*.puml` extension of the `docs/puml` directory to png.

## Result Tree

```
/docker-plantuml-generator
├── Makefile
├── README.md
├── docker
│   └── plantuml
│       ├── Dockerfile
│       ├── plantuml
│       └── requirements.txt
├── docker-compose.yml
├── docs
│   ├── .plantcache               <-- Files that have not changed will skip the conversion.
│   ├── png
│   │   └── sequence-diagram.png  <-- Generated images.
│   └── puml                      <-- The target directory is read recursively.
│       └── sequence-diagram.puml <-- Files that you do not want to convert should have an extension other than `*.puml`.
└── scripts
    └── plantuml.py
```
