// Lists all tweets containing the word “Instagram”

use("project-phase-3-db");

db.tweet.find({ text: { $regex: /Instagram/ } })
