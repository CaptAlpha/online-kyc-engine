#import Web3
from web3 import Web3, HTTPProvider
web3 = Web3(Web3.HTTPProvider('https://eth-ropsten.alchemyapi.io/v2/EodcNQJ8xVi9MHbKgwNy1PJf1dDuAL0r')) 
abi= [
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "index",
          "type": "address"
        }
      ],
      "name": "getCustomer",
      "outputs": [
        {
          "components": [
            {
              "components": [
                {
                  "internalType": "string",
                  "name": "firstName",
                  "type": "string"
                },
                {
                  "internalType": "string",
                  "name": "lastName",
                  "type": "string"
                },
                {
                  "internalType": "string",
                  "name": "DOB",
                  "type": "string"
                },
                {
                  "internalType": "string",
                  "name": "emailAddress",
                  "type": "string"
                },
                {
                  "internalType": "string",
                  "name": "homeAddress",
                  "type": "string"
                },
                {
                  "internalType": "string",
                  "name": "pancNumber",
                  "type": "string"
                },
                {
                  "internalType": "string",
                  "name": "aadharcNumber",
                  "type": "string"
                },
                {
                  "internalType": "bool",
                  "name": "verified",
                  "type": "bool"
                }
              ],
              "internalType": "struct Contract.customerDetails",
              "name": "customer_details",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "string",
                  "name": "panCard",
                  "type": "string"
                },
                {
                  "internalType": "string",
                  "name": "aadharCard",
                  "type": "string"
                },
                {
                  "internalType": "string",
                  "name": "photograph",
                  "type": "string"
                },
                {
                  "internalType": "string",
                  "name": "signature",
                  "type": "string"
                }
              ],
              "internalType": "struct Contract.customerDocs",
              "name": "customer_docs",
              "type": "tuple"
            }
          ],
          "internalType": "struct Contract.Customer",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "index",
          "type": "address"
        }
      ],
      "name": "getCustomerDetails",
      "outputs": [
        {
          "components": [
            {
              "internalType": "string",
              "name": "firstName",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "lastName",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "DOB",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "emailAddress",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "homeAddress",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "pancNumber",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "aadharcNumber",
              "type": "string"
            },
            {
              "internalType": "bool",
              "name": "verified",
              "type": "bool"
            }
          ],
          "internalType": "struct Contract.customerDetails",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "index",
          "type": "address"
        }
      ],
      "name": "getCustomerDocs",
      "outputs": [
        {
          "components": [
            {
              "internalType": "string",
              "name": "panCard",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "aadharCard",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "photograph",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "signature",
              "type": "string"
            }
          ],
          "internalType": "struct Contract.customerDocs",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "_firstName",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_lastName",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_DOB",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_emailAddress",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_homeAddress",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_pancNumber",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_aadharcNumber",
          "type": "string"
        },
        {
          "internalType": "bool",
          "name": "_verified",
          "type": "bool"
        }
      ],
      "name": "setCustomer",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "_panCard",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_aadharCard",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_photograph",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_signature",
          "type": "string"
        }
      ],
      "name": "setcustomerDocs",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]
addr = '0x168FbB42EA2A27416c9FF1F1cC2ad88704CF1073' 
contract = web3.eth.contract(address=addr, abi=abi) 
#latestData = contract.functions.latestRoundData().call() 
setdata=contract.functions.setCustomer('Arhit', 'Bose', 'Customer', 'Customer', 'Customer', 'Customer', 'Customer', True).call()
dta = contract.functions.getCustomerDetails(0).call()
print(dta)