const CustomError = 'CUSTOM ERR!';

function getLikedBrands(id){
  return new Promise((resolve, reject) => {
    // resolve([{id: 1, name: "Logestyx"}, {id: 10, name: "Gladlear"}]);
    reject(CustomError);
  });
}


function getTopBrandsForGender(gender){
  return new Promise((resolve, reject) => {
    resolve([{id: 6, name: "Burylaze Slapgalt"},{id: 1, name: "Logestyx"},{id: 7, name: "Izarpure"}]);
  });
}



function solution(U, N){
  return new Promise((resolve, reject) => {
    let resultArr = [];
    let errFlag = 0;
    getLikedBrands(U.id)
      .then((data) => {
        if(data.length === N){
          resolve(data.map(el => el.name));
        } else if(data.length < N) {
          //call getTopBrandsForGender
          resultArr = data.map(el => el.name);
          getTopBrandsForGender(U.gender)
            .then((genderBasedData) => {
              if(genderBasedData.length < (N - data.length)) {
                reject(CustomError);
              } else {
                let names = genderBasedData.map(el => el.name).slice(0, (N - data.length));
                names.forEach((el) => {
                  if(resultArr.indexOf(el) === -1){
                    resultArr.push(el);
                  }
                });
                if(resultArr.length < N){
                  // ERROR IN HERE
                  reject(CustomError);
                } else {
                  resolve(resultArr);
                }
              }
            })
            .catch((err) => {
              reject(CustomError)
            });
        } else if(data.length > N) {
          resolve(data.slice(0, N).map(el => el.name));
        }
      })
      .catch((err) => {
       reject(CustomError);
      });
  });
}



const userData = { id: 123132, gender: "FEMALE" };

solution(userData, 1)
  .then((data) => console.log(data))
  .catch((err) => console.log(err));

