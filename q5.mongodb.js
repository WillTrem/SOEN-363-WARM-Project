// This query displays the number of Twitter user created each month in the past year.
use('project-phase-3-db');

// db.userTwitter.aggregate([ 
//     {
//         $match: {
//           created: {
//             $gte: "2022-01-01",
//             $lte: "2023-01-01"
//           }
//         }
//     },
//     {
//       $group: {
//         _id: { $substr: ["$created", 0, 7] },
//         count: { $sum: 1 } 
//       }
//     },
//     {
//         $sort:
//            {
//              _id: 1
//            }
//      },
//   ])

//   db.userTwitter.aggregate([ 
//     {
//       $match: {
//         $expr: {
//           $and: [
//             { $gte: [ { $toDate: "$created" }, ISODate("2022-01-01") ] },
//             { $lte: [ { $toDate: "$created" }, ISODate("2023-01-01") ] }
//           ]
//         }
//       }
//     },
//     {
//       $group: {
//         _id: { $month: { $toDate: "$created" } },
//         count: { $sum: 1 } 
//       }
//     },
//     {
//         $sort:
//            {
//              _id: 1
//            }
//      },
//   ])
  
  