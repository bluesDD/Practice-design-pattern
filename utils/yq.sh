i=$(yq r edit_spreadsheet/.github/workflows/push.yml "jobs.gitHubActionForPylint.steps[*].name")
echo $i
