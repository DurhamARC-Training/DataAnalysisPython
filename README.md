![Course logo](img/ARC448p.png)

# Course: Data Analysis with Python

Welcome to the Data Analysis with Python repository! This repository contains all the materials and resources for the course.

## Course description

Python has become the dominant language for scientific data analysis across disciplines, from physics and biology to economics and psychology. This hands-on course teaches researchers the core Python libraries needed for this purpose: NumPy for numerical computing, pandas for data manipulation and analysis, and matplotlib for creating publication-quality visualisations. Through practical exercises using real research datasets, you'll learn to load, clean, analyse, and visualise data while exploring cases of data integrity issues in published research.
The course emphasises practical application over theory, with each topic beginning with a code-along demonstration followed by hands-on exercises. Upon completion, you'll have the foundation to integrate Python into your research workflow and access its ecosystem of specialised scientific libraries.

## Organization

The repository is organized as follows:

- `Course`: This folder contains the presentations and exercises for the course. Each topic has its own jupyter notebook with the corresponding materials.

- `Filled_Course`: This folder contains the already completed notebooks and the solutions to the exercises in the `Course` folder. It is meant for reference purposes for teaching the course and as a fallback if something is missing from the notes students made during the course.

- `Data`: This folder contains the data used during the presentation and the exercises

- `mplstyles`: Some matplotlib styles to use as examples during the course.

## Accessing the Materials

For this course we are using [JupyterLite](https://jupyterlite.readthedocs.io/en/stable/), which is a tool that allows us to launch [JupyterLab](https://jupyterlab.readthedocs.io/en/latest/) and run our Python code in the web browser through the notebook (.ipynb) files contained in this repository.

To access and run the course materials, start by:

* Navigating to the course materials on our GitHub page: https://durhamarc-training.github.io/DataAnalysisPython/

* Start by accessing the "01_Welcome.ipynb" notebook in the "Courses" directory.

You are now ready to start the course!

NOTE: The first time you run your code/load new modules, there may be a small wait while the module(s) are loaded.

## Contributing

If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request. Contributions are welcome!

You can add the files of the `common-tools` github submodule by typing in `git submodule update --init`. Consult the README in the then filled `common-tools` directory for further instructions.
In general you should never edit the content in the `Course` but work on `Filled_Course` and have the tool generate the student notebook versions automatically as described in the `common-tools` README.
