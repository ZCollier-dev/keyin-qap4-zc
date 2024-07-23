/* Create a reasonably complicated Object in JavaScript that contains attributes and methods for the Motel customer. 
The customer attributes should include (and not be limited to), the customer’s name`, birth date`, gender`, and room preferences` (as an array), payment method`, mailing address (as a sub-object)`, phone number`, check-in', and check-out' date (as a sub-object), and object methods` to determine their age' and duration of stay'.
The JavaScript code should also create a template literal string, or properly formatted html, that describes the customer. In other words, writes a paragraph describing the customer with many of their personal attributes dynamically embedded in the string / html coming from the above object definition. */

/*DESCRIPTION: Program for a motel to print customer data to a website.
AUTHOR:      Zachary Collier
DATE:        July 18th 2024*/

const customer = {
  name: "John Doe",
  birthday: new Date("1997-07-07T00:00:00"),
  gender: "Male",
  roomPrefs: ["ground floor", "minifridge"],
  payMethod: "Debit",
  mailingAddress: {
    street: "123 Main Street",
    city: "Gander",
    province: "NL",
    postalCode: "A1V0A1",
  },
  phoneNo: "(709) 123-1234",
  stayTimes: {
    checkIn: new Date("2024-07-07T00:00:00"),
    checkOut: new Date("2024-07-09T00:00:00"),
  },
  age: function() {
    this.today = new Date()
    let ageMS = this.today - this.birthday //Converts to milliseconds
    return Math.floor(ageMS / 31556952000) //Converts from milliseconds to years
  },
  stayDuration: function() {
    let stayDurationMS = this.stayTimes.checkOut - this.stayTimes.checkIn //Converts to milliseconds
    return Math.floor(stayDurationMS / 86400000) //Converts from milliseconds to days
  }
};

console.log(customer.name)
console.log(customer.gender)
console.log(customer.birthday)
console.log(customer.age())
console.log(customer.mailingAddress.street)
console.log(customer.mailingAddress.city)
console.log(customer.mailingAddress.province)
console.log(customer.mailingAddress.postalCode)
console.log(customer.phoneNo)
console.log(customer.stayTimes.checkIn)
console.log(customer.stayTimes.checkOut)
console.log(customer.stayDuration())

let paragraph = `The customer's name is ${customer.name}, ${customer.gender}, whose birthday is ${customer.birthday.getFullYear()}-${customer.birthday.getMonth()+1}-${customer.birthday.getDate()} and is thus of age ${customer.age()}. Their mailing address is ${customer.mailingAddress.street}, ${customer.mailingAddress.city} ${customer.mailingAddress.province} ${customer.mailingAddress.postalCode} and their phone number is ${customer.phoneNo}. They are paying via ${customer.payMethod}. Their room preferences are: ${customer.roomPrefs}. They are staying from ${customer.stayTimes.checkIn} to ${customer.stayTimes.checkOut}, as such their stay duration is ${customer.stayDuration()} day(s).`

document.getElementById("scriptcontent").innerHTML = paragraph


