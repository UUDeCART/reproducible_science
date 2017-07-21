# Where to find it?

    https://www.vistrails.org/index.php/Main_Page

# What is it?

An open-source scientific workflow and provenance management system that
supports data exploration and visualization.

Runs on Mac, windows and linux. Written in Python and uses the multi-platform QT library.

Comes with pylab, matplotlib, imagemagick, and other packages for visualization.

For exploratory science like simulations, data analysis and visualization, the
workflow is dynamically created and evolves rapidly. VisTrails manages the
workflow.

## Example: latex figure

Say you run a simulation and make a figure using VisTrails and embed it in your
latex document (your paper). Then a person **reading your paper**
(electronically) can click on the figure to obtain the VisTrails workflow by
clicking on it. This allows them to reproduce your simulation and recreate your
figure!

# Who uses it?

-   NASA in their climate data analysis tool.
[See](https://www.vistrails.org/images/Nasa.png)
    I tried to get the data and reproduce it, but it requires a little bit of work.
-   NSF Center for Coastal Margin Observation and Prediction
-   USGS Habitat Modeling.

# Installation

    sudo pip install vistrails PyQt4 tej scikit-learn

Or download a windows or mac installer and follow the instructions on the website. 

# Demonstration

You construct a workflow in `vt` file. I looked at `weather.vt` in the
examples directory. Open it in the gui. You can see several plots there. There
is a workflow for a "Temperature Histogram". It will display a flowchart that
does the following:

1.  It first downloads a file with the data. The url string there if you click
    on it says 

        http://www.vistrails.org/download/download.php?type=DATA&id=weather_data.zip

1.  Then it unzips the file `data.zip`.
1.  The next field describes a csv file that ought to have been unzipped. 
1.  Next, it extracts a column from the csv file called `GetTemperature` from this file.
1.  It forms a histogram using matplotlib in the usual way.
1.  Then it formats the figure, adds axes properties and sets a legend.
1.  It writes the figure to the so-called vistrails "spreadsheet"

Now, hit execute in your vistrails window. You should see a graph of a temperature histogram! This is
reproducible research, isn't it guys?!
