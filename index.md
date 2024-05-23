# Data Governance Tutorial - API

Welcome to data governance with IBM Cloud Pak for Data and IBM Knowledge Catalog.

!!! abstract "Presentation video. Choose the tab of your preferred language. "

    === "Deutsch"
        ![type:video](videos/ikc_de.mp4)
    === "Español"
        ![type:video](videos/ikc_es.mp4)
    === "English"
        ![type:video](videos/ikc_en.mp4)
    
    Unmute the sound with the control bar at the bottom of the video (speaker icon)

    Data Governance:  <https://www.ibm.com/products/cloud-pak-for-data/governance>

    IBM Knowledge Catalog: <https://www.ibm.com/products/knowledge-catalog>

## Whom I was thinking of when I wrote this tutorial?

Although I mainly thought of the technical guys at IBM and IBM Business Partners, the contents are valid and useable for everybody. It is true that some resources (the TechZone, to be more precise) are only available if you are in the close orbit of IBM but the code runs just on any Cloud Pak for Data environment if IKC has been properly deployed.

I also thought of the professionals who need to support real life projects related to Data Governance. While most of the tutorials I visited are great for starters, there is no way to accomplish the massive tasks that a big project may demand without automating, at least, some of these tasks with an API. My goal was to ease the learning curve for those who are facing the challenge of programming with the Watson Data API for the first time.

## How to use this tutorial

On the left bar, you will see the items corresponding to the suggested taks to get familiar with the Watson Data API, which is the main subject of the tutorial.

First, the Basics section. It is intended to provide code for reviewing and understanding how the API works. Needless to say, they can be perfectly used in your own projects to perform the basic taks but I wrote them to be reviewed, so that is clear which steps are necessary and how to do them.

Then, the Level 4 PoX section. This is an existing, very comprehensive tutorial written by IBM. It makes extensive use of the GUI to perform may data governance taks and, after running it completely it, it would be advisable to run this tutorial. It contains some of the PoX tasks, but implemented with the API. The intention is to compare what can be done with GUIs or with API and be able to decide in a real project which alternative is the best.

Not all tasks or sections of the PoX are implemented here. The main reason is that some of them must be done supervised by a data steward (a human, no program) and it would make no sense to run it automatically.

## Requisites for this tutorial

As stated in the introduction video, it is necessary to have a basic understanding of Data Governance (in general) and, more precisely, be familiar with the service IBM Knowledge Catalog contained in IBm Cloud Pak for Data.  

Python programming is a must, no way to scape of it. Bash programming is optional, but highly recommended.

The use of github repositories and jupyter notebooks are also a must. Otherwise, one can only read the contents. It is advisable to clone the repository on the own's laptop and execute all the tasks locally.

In the PoX section, a way to execute notebooks from the git codespaces are briefly described. A browser would be enough to run everything of this tutorial (no need for a python environment, no local jupyter server, no code editor, not even a laptop!). Think of it as an experimental feature.

Be prepared to adjust the locations of files and directories. The first lines of the jupyter notebooks will be a help (actually, a need) for customizing it to your environment. The good news is, setting at most three variables at the beginning would be enough.

And,of course, you need a Cloud Pak for Data environment where IBM Knowledge Catalog is up and running. The code would work on any of the deployed options: on any cloud, Saas, PaaS, on premise or any vaariation of these.
