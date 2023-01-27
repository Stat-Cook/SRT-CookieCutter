# SRT CookieCutter

A cookiecutter template and CLI (Command Line Interface) for use the by the Safety Research Team (SRT).

To use the CLI, first ensure you have python available and then install via:

```commandline
pip install git+https://github.com/Stat-Cook/SRT-CookieCutter
```

then - navigate the command line to where you want the root file to be and run:

```
srt_init [Project Name]
```

Replacing `[Project Name]` as needed (NB: surround values in "quotes" if it contains white space).


## Optional values:

The CLI takes a range of optional values, which can be combined as needed.

* *-wp* / *--work_packages* - The number of work packages planned
```
srt_init "Project 1" -wp 3 
```

* *-pi* / *--principal_investigator* - The name/e-mail address of the principal investigator.       
E.g:
```
srt_init "Project 2" -pi "A. N. Other"
```

* *-pm* /  *--project_manager* - The name/e-mail address of the project manager.       
E.g:
```
srt_init "Project 3" -pm "Lorus Ipsum"
```

* *-co* /  *--content_only* - An option to make ignore the top level folder.      
E.g:
```
srt_init "Project 3" -co
```
