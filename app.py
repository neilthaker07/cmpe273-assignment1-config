import sys
repoURL = str(sys.argv[1])

userRepo = repoURL[19:]
userName = userRepo.split('/')[0]
repoName = userRepo.split('/')[1]

from github import Github
g = Github()

finalRepoName = ""
finalRepo = None
for repo in g.get_user(userName).get_repos(repoName):
	if repo.name == repoName:
		finalRepoName = repo.name
		finalRepo = repo
		print repo.name

from flask import Flask
app = Flask(__name__)

@app.route("/v1/<filename>")
def get_file(filename):
	file_content = finalRepo.get_file_contents(filename)
	return file_content.decoded_content
	
if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
