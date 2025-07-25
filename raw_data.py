data_catalog = [
  {
    "database_code": "ATM",
    "database_description": "ATM database",
    "tables": [
      {
        "table_name": "atm_deposits",
        "table_description": "Atm Deposits under ATM",
        "fields": [
          {
            "field_name": "atm_id",
            "business_name": "Atm Id",
            "business_description": "Atm id related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "e8cb64bf-6a8a-45f1-b58b-a9a423ed20d0",
              "48fa4c10-e884-4444-bf00-d4e08a3c82c0",
              "cf2390f7-9e59-422a-a69e-e090ea6542b2"
            ]
          },
          {
            "field_name": "deposit_amount",
            "business_name": "Deposit Amount",
            "business_description": "Deposit amount related to banking operations.",
            "data_type": "decimal",
            "length": 10,
            "tags": [
              "atm"
            ],
            "sample_values": [
              5417.71,
              5612.22,
              1967.19
            ]
          },
          {
            "field_name": "account_number",
            "business_name": "Account Number",
            "business_description": "Account number related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "AAIO31081838429434",
              "COHN50370574715695",
              "LNNT82377768866577"
            ]
          },
          {
            "field_name": "deposit_time",
            "business_name": "Deposit Time",
            "business_description": "Deposit time related to banking operations.",
            "data_type": "timestamp",
            "length": 10,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "2021-09-12 13:35:40",
              "2022-09-20 21:22:24",
              "2022-03-22 08:10:52"
            ]
          },
          {
            "field_name": "currency",
            "business_name": "Currency",
            "business_description": "Currency related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "CAD",
              "USD",
              "EUR"
            ]
          },
          {
            "field_name": "card_last4",
            "business_name": "Card Last4",
            "business_description": "Card last4 related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "1725",
              "6848",
              "4629"
            ]
          },
          {
            "field_name": "atm_location",
            "business_name": "Atm Location",
            "business_description": "Atm location related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "when",
              "reveal",
              "ten"
            ]
          },
          {
            "field_name": "transaction_status",
            "business_name": "Transaction Status",
            "business_description": "Transaction status related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "pending",
              "active",
              "failed"
            ]
          },
          {
            "field_name": "receipt_printed",
            "business_name": "Receipt Printed",
            "business_description": "Receipt printed related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "customer",
              "bit",
              "continue"
            ]
          },
          {
            "field_name": "atm_model",
            "business_name": "Atm Model",
            "business_description": "Atm model related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "story",
              "foreign",
              "open"
            ]
          },
          {
            "field_name": "effective_start_date",
            "business_name": "Effective Start Date",
            "business_description": "Date when this record became effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "2011-06-07",
              "1983-08-06",
              "2009-02-06"
            ]
          },
          {
            "field_name": "effective_end_date",
            "business_name": "Effective End Date",
            "business_description": "Date when this record ceased to be effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "2017-04-19",
              "2018-07-01",
              "1983-08-21"
            ]
          }
        ]
      },
      {
        "table_name": "atm_event_log",
        "table_description": "Atm Event Log under ATM",
        "fields": [
          {
            "field_name": "event_id",
            "business_name": "Event Id",
            "business_description": "Event id related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "8fed68a4-153f-4ba4-9b55-d8cff15104a8",
              "6d59479d-865e-4395-ab5a-a7864f427af7",
              "7c5482f8-5500-40de-8edc-1104ef575ac5"
            ]
          },
          {
            "field_name": "atm_id",
            "business_name": "Atm Id",
            "business_description": "Atm id related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "b5735d05-a9ba-415e-9447-e593a13ace38",
              "44e7d840-7b34-4b87-8797-89070b2ed02f",
              "07c47049-cf4b-4a74-8693-b049bd70ea20"
            ]
          },
          {
            "field_name": "event_type",
            "business_name": "Event Type",
            "business_description": "Event type related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "north",
              "interest",
              "station"
            ]
          },
          {
            "field_name": "event_timestamp",
            "business_name": "Event Timestamp",
            "business_description": "Event timestamp related to banking operations.",
            "data_type": "timestamp",
            "length": 10,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "2024-03-30 17:58:45",
              "2021-06-24 04:50:11",
              "2024-06-06 21:11:03"
            ]
          },
          {
            "field_name": "component_affected",
            "business_name": "Component Affected",
            "business_description": "Component affected related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "structure",
              "place",
              "fast"
            ]
          },
          {
            "field_name": "error_code",
            "business_name": "Error Code",
            "business_description": "Error code related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "surface",
              "generation",
              "tell"
            ]
          },
          {
            "field_name": "severity_level",
            "business_name": "Severity Level",
            "business_description": "Severity level related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "wonder",
              "help",
              "movie"
            ]
          },
          {
            "field_name": "resolved_flag",
            "business_name": "Resolved Flag",
            "business_description": "Resolved flag related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "second",
              "personal",
              "cost"
            ]
          },
          {
            "field_name": "technician_id",
            "business_name": "Technician Id",
            "business_description": "Technician id related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "bcefaa29-b383-4745-93c3-1d233b75ac06",
              "b97ad398-86c5-48cc-ad43-4470132fddf9",
              "a835fdf7-1258-4ba1-bdef-11eb39ca03ac"
            ]
          },
          {
            "field_name": "notes",
            "business_name": "Notes",
            "business_description": "Notes related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "nothing",
              "trade",
              "young"
            ]
          },
          {
            "field_name": "effective_start_date",
            "business_name": "Effective Start Date",
            "business_description": "Date when this record became effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "2021-06-29",
              "1971-11-30",
              "2002-02-12"
            ]
          },
          {
            "field_name": "effective_end_date",
            "business_name": "Effective End Date",
            "business_description": "Date when this record ceased to be effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "atm"
            ],
            "sample_values": [
              "2011-06-16",
              "2010-12-22",
              "2008-06-13"
            ]
          }
        ]
      }
    ]
  },
  {
    "database_code": "WIRES",
    "database_description": "Wires database",
    "tables": [
      {
        "table_name": "outgoing_wire_payments",
        "table_description": "Outgoing Wire Payments under Wires",
        "fields": [
          {
            "field_name": "payment_id",
            "business_name": "Payment Id",
            "business_description": "Payment id related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "e6d241f6-e51f-4219-b18f-7e958470d714",
              "f25234e2-601d-41b2-b2fa-28c18505b6bc",
              "6e6f164a-ff52-4d87-8d6d-8a70c05f9e70"
            ]
          },
          {
            "field_name": "sender_account",
            "business_name": "Sender Account",
            "business_description": "Sender account related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "management",
              "kind",
              "none"
            ]
          },
          {
            "field_name": "receiver_name",
            "business_name": "Receiver Name",
            "business_description": "Receiver name related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "Lindsey Perez",
              "Judy Johns",
              "Edward Blake III"
            ]
          },
          {
            "field_name": "receiver_bank",
            "business_name": "Receiver Bank",
            "business_description": "Receiver bank related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "main",
              "he",
              "economic"
            ]
          },
          {
            "field_name": "amount",
            "business_name": "Amount",
            "business_description": "Amount related to banking operations.",
            "data_type": "decimal",
            "length": 10,
            "tags": [
              "wires"
            ],
            "sample_values": [
              7456.03,
              6884.96,
              2061.23
            ]
          },
          {
            "field_name": "currency",
            "business_name": "Currency",
            "business_description": "Currency related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "CAD",
              "USD"
            ]
          },
          {
            "field_name": "wire_date",
            "business_name": "Wire Date",
            "business_description": "Wire date related to banking operations.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "2006-11-03",
              "1996-06-21",
              "1971-06-17"
            ]
          },
          {
            "field_name": "wire_status",
            "business_name": "Wire Status",
            "business_description": "Wire status related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "pending",
              "completed",
              "active"
            ]
          },
          {
            "field_name": "initiated_by",
            "business_name": "Initiated By",
            "business_description": "Initiated by related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "gas",
              "nothing",
              "race"
            ]
          },
          {
            "field_name": "fee_applied",
            "business_name": "Fee Applied",
            "business_description": "Fee applied related to banking operations.",
            "data_type": "decimal",
            "length": 10,
            "tags": [
              "wires"
            ],
            "sample_values": [
              3905.57,
              1706.34,
              3728.4
            ]
          },
          {
            "field_name": "effective_start_date",
            "business_name": "Effective Start Date",
            "business_description": "Date when this record became effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "2020-08-07",
              "2020-04-07",
              "2022-11-12"
            ]
          },
          {
            "field_name": "effective_end_date",
            "business_name": "Effective End Date",
            "business_description": "Date when this record ceased to be effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "2023-02-22",
              "1998-07-03",
              "2005-02-20"
            ]
          },
          {
            "field_name": "beneficiary_bank_name",
            "business_name": "Beneficiary Bank Name",
            "business_description": "Name of the bank receiving the wire payment.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "Duran, Mercado and Black",
              "Gilmore-Newman",
              "Rodriguez, Day and Phillips"
            ]
          },
          {
            "field_name": "beneficiary_account_number",
            "business_name": "Beneficiary Account Number",
            "business_description": "Account number of the payment recipient.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "XSJN16703995179846",
              "NWBL39856775712019",
              "KDIH81787342212125"
            ]
          },
          {
            "field_name": "beneficiary_address",
            "business_name": "Beneficiary Address",
            "business_description": "Mailing address of the beneficiary.",
            "data_type": "string",
            "length": 100,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "48111 Hannah Mission Suite 914, Port Samanthafort, VA 60992",
              "60872 Wise Burg, South Kelsey, TN 55504",
              "84839 Petersen Prairie Apt. 169, Lisaborough, VT 76919"
            ]
          },
          {
            "field_name": "conductor_name",
            "business_name": "Conductor Name",
            "business_description": "Name of the individual initiating or conducting the transaction.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "Meghan Wilson",
              "Jo Ray",
              "Nicolas Smith"
            ]
          },
          {
            "field_name": "conductor_id_type",
            "business_name": "Conductor ID Type",
            "business_description": "Type of identification presented by the conductor.",
            "data_type": "string",
            "length": 30,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "Passport",
              "Driver's License",
              "National ID"
            ]
          },
          {
            "field_name": "conductor_id_number",
            "business_name": "Conductor ID Number",
            "business_description": "Identification number of the conductor.",
            "data_type": "string",
            "length": 30,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "837-81-8778",
              "610-54-5909",
              "362-21-2739"
            ]
          }
        ]
      },
      {
        "table_name": "incoming_wire_payments",
        "table_description": "Incoming Wire Payments under Wires",
        "fields": [
          {
            "field_name": "payment_id",
            "business_name": "Payment Id",
            "business_description": "Payment id related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "367f1618-9f01-4099-83a2-17e1bb14516a",
              "f4028e91-d3a4-4e74-beec-643017761159",
              "7150d246-28ac-4646-bc28-6d219f5abf3c"
            ]
          },
          {
            "field_name": "beneficiary_account",
            "business_name": "Beneficiary Account",
            "business_description": "Beneficiary account related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "main",
              "window",
              "someone"
            ]
          },
          {
            "field_name": "sender_name",
            "business_name": "Sender Name",
            "business_description": "Sender name related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "Samantha Harrison",
              "Lisa Brennan",
              "Molly Swanson"
            ]
          },
          {
            "field_name": "sender_bank",
            "business_name": "Sender Bank",
            "business_description": "Sender bank related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "inside",
              "plan",
              "oil"
            ]
          },
          {
            "field_name": "amount",
            "business_name": "Amount",
            "business_description": "Amount related to banking operations.",
            "data_type": "decimal",
            "length": 10,
            "tags": [
              "wires"
            ],
            "sample_values": [
              8931.63,
              5014.84,
              5495.45
            ]
          },
          {
            "field_name": "currency",
            "business_name": "Currency",
            "business_description": "Currency related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "CAD",
              "EUR"
            ]
          },
          {
            "field_name": "wire_date",
            "business_name": "Wire Date",
            "business_description": "Wire date related to banking operations.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "1999-12-24",
              "1994-03-04",
              "1978-04-12"
            ]
          },
          {
            "field_name": "confirmation_code",
            "business_name": "Confirmation Code",
            "business_description": "Confirmation code related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "heavy",
              "difference",
              "every"
            ]
          },
          {
            "field_name": "received_time",
            "business_name": "Received Time",
            "business_description": "Received time related to banking operations.",
            "data_type": "timestamp",
            "length": 10,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "2025-02-06 01:04:25",
              "2021-11-18 19:46:40",
              "2020-11-14 04:33:21"
            ]
          },
          {
            "field_name": "processing_status",
            "business_name": "Processing Status",
            "business_description": "Processing status related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "pending",
              "active",
              "inactive"
            ]
          },
          {
            "field_name": "effective_start_date",
            "business_name": "Effective Start Date",
            "business_description": "Date when this record became effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "2009-10-05",
              "2016-02-18",
              "1986-07-02"
            ]
          },
          {
            "field_name": "effective_end_date",
            "business_name": "Effective End Date",
            "business_description": "Date when this record ceased to be effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "1995-04-29",
              "2007-09-10",
              "2005-04-05"
            ]
          },
          {
            "field_name": "beneficiary_bank_name",
            "business_name": "Beneficiary Bank Name",
            "business_description": "Name of the bank receiving the wire payment.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "Case, Thompson and Tran",
              "Higgins, Bass and Williams",
              "Warren, Morgan and Anderson"
            ]
          },
          {
            "field_name": "beneficiary_account_number",
            "business_name": "Beneficiary Account Number",
            "business_description": "Account number of the payment recipient.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "QRJT51113865265005",
              "VFXE68951479537495",
              "CRJF43914727308152"
            ]
          },
          {
            "field_name": "beneficiary_address",
            "business_name": "Beneficiary Address",
            "business_description": "Mailing address of the beneficiary.",
            "data_type": "string",
            "length": 100,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "895 Cook Curve, Mariachester, NM 96852",
              "USS Floyd, FPO AP 39431",
              "9515 Eric Falls, East Clairechester, OR 28641"
            ]
          },
          {
            "field_name": "conductor_name",
            "business_name": "Conductor Name",
            "business_description": "Name of the individual initiating or conducting the transaction.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "Joshua Morris",
              "Patrick Torres",
              "Lori Moore"
            ]
          },
          {
            "field_name": "conductor_id_type",
            "business_name": "Conductor ID Type",
            "business_description": "Type of identification presented by the conductor.",
            "data_type": "string",
            "length": 30,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "Passport",
              "Driver's License",
              "National ID"
            ]
          },
          {
            "field_name": "conductor_id_number",
            "business_name": "Conductor ID Number",
            "business_description": "Identification number of the conductor.",
            "data_type": "string",
            "length": 30,
            "tags": [
              "wires"
            ],
            "sample_values": [
              "768-07-6336",
              "121-27-3805",
              "098-32-6966"
            ]
          }
        ]
      }
    ]
  },
  {
    "database_code": "CUSTOMER_INFO",
    "database_description": "Customer Info database",
    "tables": [
      {
        "table_name": "customer_info",
        "table_description": "Customer Info under Customer Info",
        "fields": [
          {
            "field_name": "customer_id",
            "business_name": "Customer Id",
            "business_description": "Customer id related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "1ec4d0fb-ddab-4848-9bfa-da98796056ea",
              "81d38859-c164-4a33-8b88-fed3df89d0bf",
              "4f749446-c3a8-4f1c-864a-803802d6c925"
            ]
          },
          {
            "field_name": "first_name",
            "business_name": "First Name",
            "business_description": "First name related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "Jessica Mann",
              "Mike Cook",
              "Benjamin Wood"
            ]
          },
          {
            "field_name": "last_name",
            "business_name": "Last Name",
            "business_description": "Last name related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "Katherine Jimenez",
              "Jeffrey Jones",
              "Dennis Huynh"
            ]
          },
          {
            "field_name": "dob",
            "business_name": "Dob",
            "business_description": "Dob related to banking operations.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "N/A"
            ]
          },
          {
            "field_name": "email",
            "business_name": "Email",
            "business_description": "Email related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "hhill@hotmail.com",
              "jparks@weaver.org",
              "thomasmoore@robinson.com"
            ]
          },
          {
            "field_name": "phone_number",
            "business_name": "Phone Number",
            "business_description": "Phone number related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "(708)343-6119",
              "+1-141-730-6470",
              "843-488-1355x65308"
            ]
          },
          {
            "field_name": "city",
            "business_name": "City",
            "business_description": "City related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "Karentown",
              "New Robertbury",
              "East Mariashire"
            ]
          },
          {
            "field_name": "postal_code",
            "business_name": "Postal Code",
            "business_description": "Postal code related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "79044",
              "65356",
              "82565"
            ]
          },
          {
            "field_name": "country",
            "business_name": "Country",
            "business_description": "Country related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "Lebanon",
              "Zambia",
              "Saudi Arabia"
            ]
          },
          {
            "field_name": "first_name",
            "business_name": "First Name",
            "business_description": "First name of the customer related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "Audrey Norris",
              "Tyler Thompson",
              "Linda Moore"
            ]
          },
          {
            "field_name": "last_name",
            "business_name": "Last Name",
            "business_description": "Last name of the customer related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "Phillip Perry",
              "Alexander Wong",
              "Thomas Gallegos"
            ]
          },
          {
            "field_name": "alias",
            "business_name": "Alias",
            "business_description": "Commonly used alias or nickname of the customer.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "car",
              "amount",
              "argue"
            ]
          },
          {
            "field_name": "street_number",
            "business_name": "Street Number",
            "business_description": "Street number of the customer's residential address.",
            "data_type": "string",
            "length": 10,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "white",
              "worker",
              "training"
            ]
          },
          {
            "field_name": "unit_number",
            "business_name": "Unit Number",
            "business_description": "Unit or apartment number of the customer.",
            "data_type": "string",
            "length": 10,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "stuff",
              "win",
              "shake"
            ]
          },
          {
            "field_name": "street_name",
            "business_name": "Street Name",
            "business_description": "Street name of the customer's address.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "Carol Foster",
              "Michael Rice",
              "Renee Collins"
            ]
          },
          {
            "field_name": "city",
            "business_name": "City",
            "business_description": "City where the customer resides.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "Danielland",
              "Williamton",
              "Williamsfort"
            ]
          },
          {
            "field_name": "province",
            "business_name": "Province",
            "business_description": "Province or state where the customer resides.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "type",
              "both",
              "industry"
            ]
          },
          {
            "field_name": "country",
            "business_name": "Country",
            "business_description": "Country of the customer's residence.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "Croatia",
              "Dominican Republic",
              "Singapore"
            ]
          },
          {
            "field_name": "effective_start_date",
            "business_name": "Effective Start Date",
            "business_description": "Date when this record became effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "2016-10-15",
              "2017-03-23",
              "2018-04-17"
            ]
          },
          {
            "field_name": "effective_end_date",
            "business_name": "Effective End Date",
            "business_description": "Date when this record ceased to be effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "1996-04-21",
              "1978-06-05",
              "1995-02-08"
            ]
          }
        ]
      },
      {
        "table_name": "employment_info",
        "table_description": "Employment Info under Customer Info",
        "fields": [
          {
            "field_name": "customer_id",
            "business_name": "Customer Id",
            "business_description": "Customer id related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "63a5966d-8778-4252-897d-690efb510cc9",
              "da1e7a56-e19c-4d83-b599-cd1268b30716",
              "dc6e15cd-7a3e-4120-94fa-a9f836db2fa7"
            ]
          },
          {
            "field_name": "employer_name",
            "business_name": "Employer Name",
            "business_description": "Employer name related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "Hoffman PLC",
              "Taylor-Thompson",
              "Brown Group"
            ]
          },
          {
            "field_name": "employment_status",
            "business_name": "Employment Status",
            "business_description": "Employment status related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "pending",
              "active",
              "completed"
            ]
          },
          {
            "field_name": "job_title",
            "business_name": "Job Title",
            "business_description": "Job title related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "identify",
              "notice",
              "on"
            ]
          },
          {
            "field_name": "annual_income",
            "business_name": "Annual Income",
            "business_description": "Annual income related to banking operations.",
            "data_type": "decimal",
            "length": 10,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              3938.12,
              611.81,
              3012.61
            ]
          },
          {
            "field_name": "employment_start_date",
            "business_name": "Employment Start Date",
            "business_description": "Employment start date related to banking operations.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "2021-11-18",
              "1978-02-14",
              "1978-06-19"
            ]
          },
          {
            "field_name": "industry",
            "business_name": "Industry",
            "business_description": "Industry related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "rather",
              "someone",
              "really"
            ]
          },
          {
            "field_name": "work_email",
            "business_name": "Work Email",
            "business_description": "Work email related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "johnsonpaula@henry.com",
              "opeterson@yahoo.com",
              "andrew28@blevins-hart.biz"
            ]
          },
          {
            "field_name": "supervisor_name",
            "business_name": "Supervisor Name",
            "business_description": "Supervisor name related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "Julie Montgomery",
              "Ryan Mcdonald",
              "David Cox"
            ]
          },
          {
            "field_name": "income_verified",
            "business_name": "Income Verified",
            "business_description": "Income verified related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "radio",
              "especially",
              "economic"
            ]
          },
          {
            "field_name": "effective_start_date",
            "business_name": "Effective Start Date",
            "business_description": "Date when this record became effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "1975-02-21",
              "1973-12-22",
              "1999-01-20"
            ]
          },
          {
            "field_name": "effective_end_date",
            "business_name": "Effective End Date",
            "business_description": "Date when this record ceased to be effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "1973-05-28",
              "1975-07-02",
              "1985-08-27"
            ]
          },
          {
            "field_name": "employment_end_date",
            "business_name": "Employment End Date",
            "business_description": "Employment end date associated with the record.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "1987-06-23",
              "1984-10-17",
              "1971-10-12"
            ]
          }
        ]
      },
      {
        "table_name": "account_info",
        "table_description": "Account Info under Customer Info",
        "fields": [
          {
            "field_name": "account_number",
            "business_name": "Account Number",
            "business_description": "Account number related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "SHEQ23250514322422",
              "RHCX60712784618985",
              "VYZY56867246349749"
            ]
          },
          {
            "field_name": "customer_id",
            "business_name": "Customer Id",
            "business_description": "Customer id related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "bd6051e1-230f-42d4-8323-e3bd6799c883",
              "d9a19e82-e111-4ba4-acca-9248b7d2cf65",
              "dc8f71ba-b723-45c9-903c-eb883734fd69"
            ]
          },
          {
            "field_name": "account_type",
            "business_name": "Account Type",
            "business_description": "Account type related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "leader",
              "case",
              "Congress"
            ]
          },
          {
            "field_name": "account_status",
            "business_name": "Account Status",
            "business_description": "Account status related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "pending",
              "active",
              "completed"
            ]
          },
          {
            "field_name": "opened_date",
            "business_name": "Opened Date",
            "business_description": "Opened date related to banking operations.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "1975-07-07",
              "1980-07-30",
              "2023-04-25"
            ]
          },
          {
            "field_name": "currency",
            "business_name": "Currency",
            "business_description": "Currency related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "CAD",
              "USD",
              "EUR"
            ]
          },
          {
            "field_name": "branch_code",
            "business_name": "Branch Code",
            "business_description": "Branch code related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "figure",
              "three",
              "can"
            ]
          },
          {
            "field_name": "linked_card_id",
            "business_name": "Linked Card Id",
            "business_description": "Linked card id related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "368b7ebc-db96-43cc-8e93-0dfd3622686e",
              "95eac4c4-7da8-43c9-bb85-89a003bf0b34",
              "f3caf5e7-577d-41d1-a341-65ced6a12660"
            ]
          },
          {
            "field_name": "current_balance",
            "business_name": "Current Balance",
            "business_description": "Current balance related to banking operations.",
            "data_type": "decimal",
            "length": 10,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              9715.43,
              276.81,
              8985.47
            ]
          },
          {
            "field_name": "overdraft_enabled",
            "business_name": "Overdraft Enabled",
            "business_description": "Overdraft enabled related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "start",
              "garden",
              "approach"
            ]
          },
          {
            "field_name": "effective_start_date",
            "business_name": "Effective Start Date",
            "business_description": "Date when this record became effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "1974-09-23",
              "1985-03-19",
              "1988-01-13"
            ]
          },
          {
            "field_name": "effective_end_date",
            "business_name": "Effective End Date",
            "business_description": "Date when this record ceased to be effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "customer_info"
            ],
            "sample_values": [
              "2019-11-05",
              "1992-11-29",
              "1996-06-18"
            ]
          }
        ]
      }
    ]
  },
  {
    "database_code": "DEPOSIT_ACCOUNT",
    "database_description": "Deposit Account database",
    "tables": [
      {
        "table_name": "deposit_accounting_transactions",
        "table_description": "Deposit Accounting Transactions under Deposit Account",
        "fields": [
          {
            "field_name": "transaction_id",
            "business_name": "Transaction Id",
            "business_description": "Transaction id related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "deposit_account"
            ],
            "sample_values": [
              "05dfe65a-f10d-435c-8153-e16daf65c8ab",
              "777c036b-8380-49bb-a780-43ad3c693bfc",
              "119021e6-938f-46f9-a1b3-da4c9767d97e"
            ]
          },
          {
            "field_name": "account_number",
            "business_name": "Account Number",
            "business_description": "Account number related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "deposit_account"
            ],
            "sample_values": [
              "RZDP65007137932964",
              "RWEU40212073150224",
              "TOMG89494077773621"
            ]
          },
          {
            "field_name": "transaction_type",
            "business_name": "Transaction Type",
            "business_description": "Transaction type related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "deposit_account"
            ],
            "sample_values": [
              "public",
              "according",
              "goal"
            ]
          },
          {
            "field_name": "transaction_amount",
            "business_name": "Transaction Amount",
            "business_description": "Transaction amount related to banking operations.",
            "data_type": "decimal",
            "length": 10,
            "tags": [
              "deposit_account"
            ],
            "sample_values": [
              9535.09,
              302.43,
              4761.81
            ]
          },
          {
            "field_name": "transaction_date",
            "business_name": "Transaction Date",
            "business_description": "Transaction date related to banking operations.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "deposit_account"
            ],
            "sample_values": [
              "2007-03-14",
              "2016-10-28",
              "2016-11-21"
            ]
          },
          {
            "field_name": "reference_number",
            "business_name": "Reference Number",
            "business_description": "Reference number related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "deposit_account"
            ],
            "sample_values": [
              "impact",
              "finally",
              "color"
            ]
          },
          {
            "field_name": "branch_id",
            "business_name": "Branch Id",
            "business_description": "Branch id related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "deposit_account"
            ],
            "sample_values": [
              "9c261621-6d8a-4ff5-954d-0730d03832db",
              "bc3c506e-739f-4221-8bcd-416795371d62",
              "f336db93-e50f-4919-9351-65953178003f"
            ]
          },
          {
            "field_name": "teller_id",
            "business_name": "Teller Id",
            "business_description": "Teller id related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "deposit_account"
            ],
            "sample_values": [
              "abb30db5-3d7a-4379-adc6-b8debd52e11d",
              "0489b51a-0a03-4a79-aad6-7aa3985bab12",
              "db3de587-f946-4498-a708-10d25a5df812"
            ]
          },
          {
            "field_name": "approval_status",
            "business_name": "Approval Status",
            "business_description": "Approval status related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "deposit_account"
            ],
            "sample_values": [
              "pending",
              "active",
              "failed"
            ]
          },
          {
            "field_name": "posting_date",
            "business_name": "Posting Date",
            "business_description": "Posting date related to banking operations.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "deposit_account"
            ],
            "sample_values": [
              "2003-12-17",
              "1989-09-07",
              "1995-02-26"
            ]
          },
          {
            "field_name": "effective_start_date",
            "business_name": "Effective Start Date",
            "business_description": "Date when this record became effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "deposit_account"
            ],
            "sample_values": [
              "1975-04-10",
              "1990-06-17",
              "1971-11-20"
            ]
          },
          {
            "field_name": "effective_end_date",
            "business_name": "Effective End Date",
            "business_description": "Date when this record ceased to be effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "deposit_account"
            ],
            "sample_values": [
              "2014-03-19",
              "1995-09-16",
              "1998-03-27"
            ]
          }
        ]
      }
    ]
  },
  {
    "database_code": "BILL_PAYMENTS",
    "database_description": "Bill Payments database",
    "tables": [
      {
        "table_name": "bill_payment_transaction_logs",
        "table_description": "Bill Payment Transaction Logs under Bill Payments",
        "fields": [
          {
            "field_name": "payment_id",
            "business_name": "Payment Id",
            "business_description": "Payment id related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "bill_payments"
            ],
            "sample_values": [
              "5e7501c5-0615-444c-9973-ac4c74ca3f62",
              "2d100ded-2290-49b6-a514-72e12c170afc",
              "a577f539-c38f-46e8-9ebd-c03f6a0b1d76"
            ]
          },
          {
            "field_name": "biller_name",
            "business_name": "Biller Name",
            "business_description": "Biller name related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "bill_payments"
            ],
            "sample_values": [
              "Daniel Tucker",
              "Stephen Mcdaniel",
              "Amber Thompson"
            ]
          },
          {
            "field_name": "account_number",
            "business_name": "Account Number",
            "business_description": "Account number related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "bill_payments"
            ],
            "sample_values": [
              "AKDE40052569076305",
              "FMWO47806589958139",
              "VTJC82296623357814"
            ]
          },
          {
            "field_name": "payment_amount",
            "business_name": "Payment Amount",
            "business_description": "Payment amount related to banking operations.",
            "data_type": "decimal",
            "length": 10,
            "tags": [
              "bill_payments"
            ],
            "sample_values": [
              9506.25,
              6409.28,
              9035.95
            ]
          },
          {
            "field_name": "payment_date",
            "business_name": "Payment Date",
            "business_description": "Payment date related to banking operations.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "bill_payments"
            ],
            "sample_values": [
              "1982-04-22",
              "1984-01-19",
              "1975-12-07"
            ]
          },
          {
            "field_name": "payment_status",
            "business_name": "Payment Status",
            "business_description": "Payment status related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "bill_payments"
            ],
            "sample_values": [
              "pending",
              "completed",
              "active"
            ]
          },
          {
            "field_name": "confirmation_number",
            "business_name": "Confirmation Number",
            "business_description": "Confirmation number related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "bill_payments"
            ],
            "sample_values": [
              "establish",
              "minute",
              "financial"
            ]
          },
          {
            "field_name": "auto_pay_flag",
            "business_name": "Auto Pay Flag",
            "business_description": "Auto pay flag related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "bill_payments"
            ],
            "sample_values": [
              "until",
              "claim",
              "do"
            ]
          },
          {
            "field_name": "customer_id",
            "business_name": "Customer Id",
            "business_description": "Customer id related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "bill_payments"
            ],
            "sample_values": [
              "cd3f8180-5467-456c-b163-b290876996d5",
              "0ac2dd27-8d58-4cb3-bb2d-b54ca9c395f7",
              "d95d6b73-4812-4b0b-9122-eac4d1bc0373"
            ]
          },
          {
            "field_name": "biller_category",
            "business_name": "Biller Category",
            "business_description": "Biller category related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "bill_payments"
            ],
            "sample_values": [
              "budget",
              "avoid",
              "rock"
            ]
          },
          {
            "field_name": "effective_start_date",
            "business_name": "Effective Start Date",
            "business_description": "Date when this record became effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "bill_payments"
            ],
            "sample_values": [
              "1972-01-23",
              "1991-12-05",
              "1995-10-30"
            ]
          },
          {
            "field_name": "effective_end_date",
            "business_name": "Effective End Date",
            "business_description": "Date when this record ceased to be effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "bill_payments"
            ],
            "sample_values": [
              "1996-07-06",
              "1981-03-03",
              "1986-02-26"
            ]
          }
        ]
      }
    ]
  },
  {
    "database_code": "VISA_TRANSACTIONS",
    "database_description": "Visa Transactions database",
    "tables": [
      {
        "table_name": "visa_transactional_data",
        "table_description": "Visa Transactional Data under Visa Transactions",
        "fields": [
          {
            "field_name": "transaction_id",
            "business_name": "Transaction Id",
            "business_description": "Transaction id related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "visa_transactions"
            ],
            "sample_values": [
              "9abac2f7-1e06-4731-a30d-e0c8d3834478",
              "05cdb645-7274-4974-9485-d936e56268b5",
              "44e8e39d-a0ec-4ddc-acc8-3cef74a18009"
            ]
          },
          {
            "field_name": "card_number_last4",
            "business_name": "Card Number Last4",
            "business_description": "Card number last4 related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "visa_transactions"
            ],
            "sample_values": [
              "8564",
              "4830",
              "4473"
            ]
          },
          {
            "field_name": "merchant_name",
            "business_name": "Merchant Name",
            "business_description": "Merchant name related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "visa_transactions"
            ],
            "sample_values": [
              "Davis-Cannon",
              "Morgan Group",
              "Smith, Webb and Cobb"
            ]
          },
          {
            "field_name": "transaction_amount",
            "business_name": "Transaction Amount",
            "business_description": "Transaction amount related to banking operations.",
            "data_type": "decimal",
            "length": 10,
            "tags": [
              "visa_transactions"
            ],
            "sample_values": [
              5184.75,
              5418.84,
              2859.49
            ]
          },
          {
            "field_name": "transaction_currency",
            "business_name": "Transaction Currency",
            "business_description": "Transaction currency related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "visa_transactions"
            ],
            "sample_values": [
              "CAD",
              "USD",
              "EUR"
            ]
          },
          {
            "field_name": "transaction_date",
            "business_name": "Transaction Date",
            "business_description": "Transaction date related to banking operations.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "visa_transactions"
            ],
            "sample_values": [
              "1989-05-07",
              "1974-03-03",
              "2001-01-28"
            ]
          },
          {
            "field_name": "authorization_code",
            "business_name": "Authorization Code",
            "business_description": "Authorization code related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "visa_transactions"
            ],
            "sample_values": [
              "organization",
              "form",
              "memory"
            ]
          },
          {
            "field_name": "merchant_category_code",
            "business_name": "Merchant Category Code",
            "business_description": "Merchant category code related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "visa_transactions"
            ],
            "sample_values": [
              "whether",
              "wrong",
              "scene"
            ]
          },
          {
            "field_name": "foreign_transaction_flag",
            "business_name": "Foreign Transaction Flag",
            "business_description": "Foreign transaction flag related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "visa_transactions"
            ],
            "sample_values": [
              "program",
              "adult",
              "others"
            ]
          },
          {
            "field_name": "customer_id",
            "business_name": "Customer Id",
            "business_description": "Customer id related to banking operations.",
            "data_type": "string",
            "length": 50,
            "tags": [
              "visa_transactions"
            ],
            "sample_values": [
              "754679a2-b369-45ef-b51e-b3e8ebf46a2d",
              "448fd43e-d42e-453f-aa8e-dccbef264941",
              "abe1ae30-e73c-432d-b2fc-297abdf8eb75"
            ]
          },
          {
            "field_name": "effective_start_date",
            "business_name": "Effective Start Date",
            "business_description": "Date when this record became effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "visa_transactions"
            ],
            "sample_values": [
              "2002-08-20",
              "1979-09-04",
              "1999-01-15"
            ]
          },
          {
            "field_name": "effective_end_date",
            "business_name": "Effective End Date",
            "business_description": "Date when this record ceased to be effective.",
            "data_type": "date",
            "length": 10,
            "tags": [
              "visa_transactions"
            ],
            "sample_values": [
              "2025-05-31",
              "2007-07-27",
              "1994-06-19"
            ]
          }
        ]
      }
    ]
  }
]