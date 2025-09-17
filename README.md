
# Static Site Generator

[Boot.dev guided project](https://www.boot.dev/courses/build-static-site-generator-python) for building a static site generator from scratch in Python

[📜 Certificate of Completion](https://www.boot.dev/certificates/b9eb9f25-84a5-4566-ba1a-7981c61b13e1)

## Run Locally

### Prerequisites

- Python

Clone the project.

```bash
git clone https://github.com/joshjavier/ssg-python
```

Go to the project directory.

```bash
cd ssg-python
```

Run it!

```bash
./main.sh
```
## Build and Deployment

This project uses GitHub Pages for deployment.

First, build the static files into the `docs` directory.

```bash
./build.sh
```

Then, commit the generated files.

```bash
git commit -m "build"
```

Finally, push to the `main` branch.

```bash
git push
```

**Note:** Make sure your settings are set to build your GitHub Pages site from the `/docs` folder in the `main` branch.