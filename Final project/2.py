# -*- coding: utf-8 -*-

# -- Editor --

# Исследуйте функции:
# f = 2 * x ** 3 + 2 * x ** 2 - 18 * x -18

from sympy import *
# from sympy.abc import x, y, f, g
# from sympy import Symbol, sin, cos

from sympy.plotting import plot

init_printing()

x = Symbol('x')
f = 2 * x ** 3 + 2 * x ** 2 - 18 * x -18
a = plot(f, (x, -0.8, 5))

# Нули функции
solveset(f, x)

# Найти интервалы
b = [-oo, oo]
b[1:1] = solve(diff(f), x)
b

# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
c = []
d = []
for i in range(1, len(b)):
    boo = is_increasing(f, Interval.open(b[i-1], b[i]))
    if boo:
        c.append(f"{b[i-1]} {b[i]}")
    else:
        d.append(f"{b[i-1]} {b[i]}")
print('Возрастает в диапазоне', c)
print('Убывает в диапазоне', d)

# 5. Вычислить вершину
# Экстремумы функции
e = solve(diff(f), x)
for i in e:
    g = f.subs(x, i)
    if g < 0:
        print(f'Нижний экстремум: x:{i} y:{g}')
    elif g > 0:
        print(f'Верхний экстремум: x:{i} y:{g}')
a = plot(f, (x, -1.5, 1.5))

# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0
# Знакопостоянства функции
m = [-oo, oo]

incr_list = []
decr_list = []
m[1:1] = solve(f, x)
for i in range(1, len(m)):
    boo = is_increasing(f, Interval.open(m[i-1], m[i]))
    if boo:
        incr_list.append(f'{m[i-1]}, {m[i]}')
    else:
        decr_list.append(f'{m[i-1]}, {m[i]}')

# print(f'{0}{1}{2}{3}{0}', *h)

print("f > 0:", *incr_list, sep="\n")
print("f < 0:", *decr_list, sep="\n")

# -- Data --

# # Working with data
# ## Video tutorial
#
# <div align="center"><video width="800" height="450" controls>
#
# <source src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos_new/2_Working_with_Data.mp4">
#
# </video></div>


#
# ## Plug in multiple data sources
#
# In Datalore you can work with **various data sources** together in one notebook.
#
# You can connect your **SQL databases** (such as MySQL, Snowflake, PostgreSQL, Redshift, etc.), **bucket storages** (AWS S3, GCS buckets), and **files** (any file types) from the interface and further query and join them in one notebook.
#
# To manage all your data, please use the **Attached data** tab in the left-hand sidebar.
#
# <div><img src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos_new/many_datasets2.png" width = 1000 border="2" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


# ## Reusing data connections
#
# When creating a bucket or a database connection, you’ll be able to reuse it across other notebooks in the same workspace.
#
# You can manage all of the attached data sources from the workspace file system and add new connections directly from the notebook interface.
#
# When you share a notebook or a workspace, your credentials **are not exposed to the environment**.
#
# <div><img src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos_new/manage_datasources2.png" width = 600 border="2" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


# ## Persistent file storage
#
# Datalore comes with persistent storage for each notebook. This means you can upload your data files directly to **Notebook files**. If you want to share a file across multiple notebooks, attach **Workspace files** to the notebook and upload it there. Workspace files are mounted under the `/data/workspace_files/` directory.
#
# ### Benefits of attaching files to a notebook
#
# - Your workspace file system won't be cluttered with too many files.
# - Notebook files are shared automatically when you invite collaborators to the notebook.
#
# Additionally, you can download data to Notebook or Workspace files or to store it in memory using various Python packages and APIs.


# ## Dataframe exploration
#
# Whenever a pandas dataframe is the result of your cell execution, you get additional tabs in the cell output:
# - **Table** – a scrollable table view of your data
# - **Raw** – this tab represents the raw output without the ability to scroll the data
# - **Visualize** – this tab brings out-of-the box plots to help you visually explore the data
# - **Statistics** – this tab provides essential descriptive statistics for your dataframe
#
# ### Task: **Run the code cell above** and navigate to the **Visualize** and **Statistics** tabs!
#
# <div><img src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos_new/statistics_new2.png" width = 600 border="2" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


import urllib
import pandas as pd

urllib.request.urlretrieve('https://datalore-samples.s3.eu-west-1.amazonaws.com/datalore_gallery_of_samples/Getting+started/gpus.csv', 'gpus.csv')

data = pd.read_csv("gpus.csv")
data

# ## Viewing and editing attached files
#
# Double-clicking on a .csv or text file opens it for editing in the right sidebar editor and lets you view the file and edit its contents.
#
# <div><img src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos_new/edit_csv_new2.png" width = 600 border="2" style="border-color: #d3d3d3; margin-top: 1%;"/></div>
#
# If you open a .py script, you will also get smart coding assistance features for editing its contents.
#
# <div><img src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos_new/python_func2.png" width = 600 border="2" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


# -- Environment --

# # Managing the environment


# ## Video tutorial
#
# <div align="center"><video width="800" height="450" controls>
#
# <source src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos_new/3_Configuring_Environment_in_Datalore.mp4">
#
# </video></div>


# ## Preconfigured environment
#
# Each notebook in Datalore has an **isolated environment**. This means that when you apply changes to one notebook, they won't affect any of the other notebook environments.
#
# Datalore comes with a lot of **Python libraries pre-installed**.
#
# We've already installed `pandas`, `NumPy`, `sklearn`, `MatplotLib`, and `Seaborn`, so you can start importing the package you need right away.
#
# Datalore supports both the **pip** and **Conda** package managers. Pip is chosen by default, but you can always switch to Conda.
#
# <div><img src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos_new/environment_tab.png" width = 300 border="2" style="border-color: #d3d3d3; margin-top: 1%;"/></div>
#
# ## Installing additional libraries
#
# - To install additional libraries, upgrade package versions, and remove libraries, go to *Environment | Explore tab*. The changes will be written into the .yaml file, which will be stored in your Notebook files.
# - To install a package from a Git repository, go to *Environment | Repositories*.
# - To install any other dependencies (f.e. non-python dependencies), you can modify the `init.sh` file. It will run before the environment is installed.
#
# 💡 Packages installed via the **Environment** tab are **persisted** when you reopen notebooks. You can also install packages using **pip magic commands** or ***Terminal***, but they won't be persisted.
#
# You can learn more about this in the [Environment manager documentation.](https://www.jetbrains.com/help/datalore/environment.html)


# ### Task: Install and import the `datasets` library
#
# 1. Run the code cell below using `Shift+Enter`.
# 2. **Click on the prompt in the error log to search for the datasets library. This prompt will open the *Explore tab* of the *Environment manager*.**
# 3. Click on the datasets library.
# 4. Click the Install button.
# 5. Restart the kernel.
# 6. Rerun the cell.


import datasets

datasets.__version__

# -- Sharing --

# # Collaborating with your team
#
# ## Video tutorial
#
# <div align="center"><video width="800" height="450" controls>
#
# <source src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos_new/4_Sharing_Notebooks_and_Workspaces_in_Datalore.mp4">
#
# </video></div>


# ## Sharing a notebook
#
# In Datalore, you can edit notebooks together with your team in real time.
#
# Click on the Share button in the top-right corner and choose your preferred sharing method:
# - Share by sending a link (the simpler option).
# - Invite collaborators by email (for more granular permissions).
# - Share with groups of collaborators. Please contact your Datalore admins to find out whether you have groups integrated with Datalore.
#
# 💡 To access notebooks as collaborators, invited users will need to create a Datalore account.
#
# <div><img src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos_new/Sharing2.png" width = 900 border="2" style="border-color: #d3d3d3; margin-top: 1%;"/></div>
#
# When sharing a notebook you can provide either edit or view access.
# - **Edit access** will allow collaborators to edit code and attached files and run computations.
#
#   ⚠️ Note that collaborators will consume the notebook owner's resources.
# - **View access** will only allow users to see the real-time representation of the notebook.
#
# To track the changes, Datalore has a **built-in version control system** where you can create history checkpoints and revert the notebook to past versions. Check this out via ***Tools | History***.
#
# You can read more about notebook sharing [here](https://www.jetbrains.com/help/datalore/share-a-notebook.html).


# ### Task: Invite your colleagues to Datalore!
#
# Try out the real-time collaboration feature with your colleagues. Working together can be a lot of fun. 🚀
#
# To **track your collaborator's actions** through the notebook and attached files, click on their avatar in the upper right-hand corner and start following along!
#
# <div><img src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos_new/Main_teamwork.png" width = 900 border="2" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


# ## Sharing a workspace
#
# In Datalore, you can create and share workspaces.
#
# Workspaces help you organize your work and allow you to easily share multiple notebooks, data connections, files, and reports with your team.
#
#
# <div><img src="https://datalore-samples.s3.eu-west-1.amazonaws.com/datalore_gallery_of_samples/Getting+started/workspace.png" width = 300 border="2" style="border-color: #d3d3d3; margin-top: 1%;"/></div>
#
# ⚠️ Note that the workspace owner's resources will be consumed for all the computations made in the workspace.


# -- Reporting --

# # Reporting
#
# ## Video tutorial
#
# <div align="center"><video width="800" height="450" controls>
#
# <source src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos_new/5_Creating_Interactive_Reports_with_Datalore.mp4">
#
# </video></div>


#
# ## Report builder
#
# To share your research results with stakeholders, you can use the Report builder feature via the *Tools* menu section or by clicking the *Build report* button in the upper right-hand corner.
#
# You will be able to:
# - Arrange the cells on a canvas to make the report look more dashboard-style.
# - Hide specific cell inputs and outputs.
# - Publish a static or interactive report.
#
# <div><img src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos_new/Report_builder2.png" width = 900 border="2" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


# ### Task: Create a report out of this notebook!


# ## Sharing reports
# After you publish a report, it will become available under a link. You can then share it with colleagues even if they don't have a Datalore account – the report will be available for them inside the browser. Each report viewer will get a separate copy of the report and will be able to interact with the controls and rerun the report independently.
#
# You can also access **all the workspace reports** from the Published reports section in your Workspace file system.


# ## Export as PDF, PY, IPYNB
#
# You can export notebooks in multiple formats, including PDF.
#
# Go to the *File* menu tab and select the export option you need.


# -- Automations --

# # Automations
#
# ## Video tutorial
#
# <div align="center"><video width="800" height="450" controls>
#
# <source src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos_new/6_Creating_Schedules_and_Configuring_Computation_in_Datalore.mp4">
#
# </video></div>


# ## Scheduled runs
#
# In Datalore, you can schedule your notebook to run on a regular basis. Go to the Computation tab and create a schedule in the Scheduled runs widget. You'll be able to configure the running interval by using the dropdowns or by specifying a cron string.
#
# <div><img src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos_new/scheduling2.png" width = 900 border="2" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


# ### Scheduled report updates
#
# When configuring notebook schedules, you can choose to automatically update published reports, delivering regular updates to your stakeholders.
#
# ### Managing the schedules
#
# You can view and edit all the schedules of the workspace from the file system. You'll be able to view your run results and change the scheduling settings.


# ## Switching between CPU and GPU
#
# When running a notebook, you can choose between available machines according to your needs. The Computation tab will also show you the CPU and RAM load statistics. The computation status bar is located in the bottom right-hand corner of the editor.
#
# <div><img src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos_new/Changing_machine_type.png" width = 300 border="2" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


# ## Background computation
#
# Switching on Background computation from the Computation tab allows you to keep notebooks running even if you close the browser tab.
#
# Learn more about Background computation [here](https://helpserver.labs.jb.gg/help/datalore/machine-management.html#computation-modes).
#
# ⚠️ Be careful when switching on Background computation, as it will consume your computation quota.


# ## Shortcuts 101
#
# Datalore supports a wide variety of Jupyter and PyCharm shortcuts. You can access the full list from *Help | Shortcuts* or by pressing `Shift+F1`.
#
# <div><img src="https://datalore-samples.s3.eu-west-1.amazonaws.com/datalore_gallery_of_samples/Getting+started/Shortcuts.png" width = 300 border="1" style="border-color: #d3d3d3; margin-top: 1%;"/></div>
#
# ### Command mode and Editor mode
#
# There are two modes for shortcuts: Command mode and Editor mode.
#
# When editing a cell's content you are in Editor mode. To access Command mode, which allows you to manipulate the cells themselves, press `Esc`. To switch back to Editor mode, press `Enter`.


# ### Some of the most often used shortcuts include:
#
# - Run the selected cell and select below: `Shift+Enter`.
# - Change cell type: `Command+M/Ctrl+M`.
# - Undo action: `Command+Z/Ctrl+Z`.
# - Delete cell: `DD` (Command mode).
# - Insert cell above: `A` (Command mode).
# - Insert cell below: `B` (Command mode).
# - Copy selected cells: `C` (Command mode).
# - Cut selected cells: `X` (Command mode).
# - Paste below: `V` (Command mode).


# ### Command palette
#
# Access quick actions using the Command palette from the Help menu tab.
#
# <div><img src="https://datalore-samples.s3.eu-west-1.amazonaws.com/datalore_gallery_of_samples/Getting+started/Command_palette.png" width = 300 border="1" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


# -- Tutorials --

# # Tutorial Gallery, Updates, Contact info
#
# We regularly post tips & tricks on our [blog](https://blog.jetbrains.com/datalore/) and on[Twitter](https://twitter.com/Datalore)! Check them out and subscribe to get the most out of Datalore.
#
# ## Basic tutorials
#
# - [Pandas Tutorial: 10 Most Popular Questions for Python Data Frames](https://datalore.jetbrains.com/view/notebook/6gojhrbqOlQNBil7H542XF)
# - [Visualization Tutorial With Seaborn](https://datalore.jetbrains.com/view/notebook/v8mLoENq8XTfmStTCLNMV6)
# - [Visualization With Pyplot in Datalore](https://datalore.jetbrains.com/view/notebook/Rk9o3SlkJAd47e8plzm0dV)
# - [Interactive Controls Tutorial](https://datalore.jetbrains.com/view/notebook/sQPS7uBqNrBiu7t7uQXV74)
# - [Lets-Plot Usage Guide](https://datalore.jetbrains.com/view/notebook/nsYaTYEEYG1wGIaqa2bWr5)
# - [Exploratory Data Analysis in Practice](https://blog.jetbrains.com/datalore/2022/09/05/exploratory-data-analysis-in-practice/)
#
# ## Cool notebook samples
#
# - [10,000,000 Jupyter Notebooks Analyzed](https://datalore.jetbrains.com/view/notebook/F7aMWFiuETFIWCo9BoxAtv)
# - [Random Forest, Trees, and Stumps 🌳🌴🌲 A General Overview of Binary Classification Models](https://datalore.jetbrains.com/view/notebook/feUEhlTKRkbohY59fq18fN)
#
# ## Webinars
# - [Is Your Analysis Reproducible? 5 Ways to Make Your Work Bulletproof With Datalore](https://www.youtube.com/watch?v=MIctg07feIc)
# - [5 Tips for Combining Python and SQL in Datalore](https://www.youtube.com/watch?v=5lPTshUFpW8)
#
# ## Video Tutorials
# - [5 tips for using SQL cells in Datalore](https://www.youtube.com/watch?v=xHlahGVq_BE)
# - [5 Tips for Creating Interactive Reports with Python in Datalore](https://www.youtube.com/watch?v=cyYpQMRUOdE)


# ## How to get support
#
# What really helps us make the Datalore product better is your feedback. Our team is always thankful when you tell us about your experience or report bugs.
#
# Feel free to share your feedback with us and report any issues by:
#
# - Writing a post on our [public forum](https://datalore-forum.jetbrains.com/).
# - Emailing us at datalore-enterprise@jetbrains.com.


