# yes_no.js
Web-API for [yesno.wtf](https://yesno.wtf) website which can generate yes or no randomly

## Example
```JavaScript
async function main() {
	const { YesNo } = require("./yes_no.js")
	const yesNo = new YesNo()
	const answer = await yesNo.getAnswer()
	console.log(answer)
}

main()
```
