# GitCommitter

Commiter is an application that allows you to create as many as files as you want and commit them in your git repasitory.<br />
Basically you can use this app to create fake commits on your github profile at any date that you want.

## Project set up
You can clone this repository and run the <b><i>GitSet.sh</i></b> file to begin the application setup.
```shell
chmod +x ./Setups/GitSet.sh
```

And then run the bash file:
```shell
./Setups/GitSet.sh
```

After that you need to give the application a link to your repository at github.<br />
And then you just run the committer file to run the application.
```shell
python Committer.py
```

## How it works ?
Well after you entered the github repository link, it will ask you to choose the files you want to create for commit.<br />
Then it will ask you for the number of that files.<br />
In the end you just need to enter a data for your commit to be pushed.<br />
The application will add the files and commit them, after that it pushes the commits to your github repository and thats it.<br />
Application also uses a cache, so it will save your old commits in case you want to repeat theme again with a different date.<br />
