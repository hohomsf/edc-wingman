data_catalog = [
    {
        "table": "Customer",
        "tabledesc": "Contains customer details.",
        "columns": ["customer_id", "name", "address", "email", "phone_number"]
    },
    {
        "table": "Orders",
        "tabledesc": "Tracks customer orders.",
        "columns": ["order_id", "product_id", "customer_id", "quantity", "order_date"]
    },
    {
        "table": "Products",
        "tabledesc": "List of products with detailed specifications.",
        "columns": ["product_id", "name", "category", "price", "stock_quantity"]
    },
    {
        "table": "Employees",
        "tabledesc": "Contains employee data.",
        "columns": ["employee_id", "name", "department", "email", "hire_date"]
    },
    {
        "table": "Shipping",
        "tabledesc": "Includes shipping information.",
        "columns": ["shipment_id", "order_id", "carrier", "tracking_number", "delivery_status"]
    },
    {
        "table": "Invoices",
        "tabledesc": "Stores billing data for customers.",
        "columns": ["invoice_id", "customer_id", "amount_due", "due_date", "payment_status"]
    },
    {
        "table": "Payments",
        "tabledesc": "Tracks payment activity.",
        "columns": ["payment_id", "invoice_id", "method", "amount_paid", "payment_date"]
    },
    {
        "table": "Vendors",
        "tabledesc": "Details about external vendors.",
        "columns": ["vendor_id", "name", "contact_person", "phone_number", "address"]
    },
    {
        "table": "Inventory",
        "tabledesc": "Tracks inventory levels and stock control.",
        "columns": ["item_id", "location", "quantity_on_hand", "reorder_level", "last_updated"]
    },
    {
        "table": "Returns",
        "tabledesc": "Handles returned items.",
        "columns": ["return_id", "order_id", "product_id", "reason", "return_date"]
    },
    {
        "table": "Categories",
        "tabledesc": "Defines product categories.",
        "columns": ["category_id", "name", "description", "parent_category_id", "status"]
    },
    {
        "table": "Discounts",
        "tabledesc": "Manages promotional discounts.",
        "columns": ["discount_id", "description", "amount", "start_date", "end_date"]
    },
    {
        "table": "Warehouses",
        "tabledesc": "Stores warehouse details.",
        "columns": ["warehouse_id", "name", "location", "capacity", "manager"]
    },
    {
        "table": "Departments",
        "tabledesc": "Details organizational departments.",
        "columns": ["department_id", "name", "head", "budget", "location"]
    },
    {
        "table": "Projects",
        "tabledesc": "Tracks business projects.",
        "columns": ["project_id", "name", "department_id", "start_date", "end_date"]
    },
    {
        "table": "TimeSheets",
        "tabledesc": "Logs employee work hours.",
        "columns": ["timesheet_id", "employee_id", "date", "hours_worked", "project_id"]
    },
    {
        "table": "SupportTickets",
        "tabledesc": "Manages customer support tickets.",
        "columns": ["ticket_id", "customer_id", "issue_description", "status", "opened_date"]
    },
    {
        "table": "AuditLogs",
        "tabledesc": "Records system activity logs.",
        "columns": ["log_id", "user_id", "action", "timestamp", "ip_address"]
    },
    {
        "table": "Compliance",
        "tabledesc": "Contains compliance and policy information.",
        "columns": ["compliance_id", "policy_name", "status", "last_reviewed", "owner"]
    },
    {
        "table": "Analytics",
        "tabledesc": "Houses analytical report data.",
        "columns": ["report_id", "metric_name", "value", "date_generated", "created_by"]
    }
]
