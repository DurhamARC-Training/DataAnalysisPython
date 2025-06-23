# Course Data Analysis in Python

Welcome to the Course "Data Analysis in Python" repository! This repository contains all the materials and resources for the course.

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

* On the left side bar, find and open the "Courses" folder, and then open the file "01_Welcome.ipynb"

You are now ready to start the course!

NOTE: The first time you run your code/load new modules, there may be a small wait while the module(s) are loaded.

## Contributing

If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request. Contributions are welcome!

You can add the files of the `common-tools-for-teaching` github submodule by typing in `git submodule update --init`. Consult the README in the then filled `common-tools` directory for further instructions.
In general you should never edit the files contained within the `Course` folder, but work on `Filled_Course` and have the tool generate the student notebook  versions automatically.
