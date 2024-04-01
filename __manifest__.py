{
     "name":"Daily Orders",
     "summary":"it display daily orders",
    #  "Website":"www.google.com",
     "depends":["mail"],
     "category": "Sales",
     "depends": ["sale"],
     "data":[
                "secuirty/ir.model.access.csv",
                "data/sequence.xml",
                "views/menu.xml",
                "views/order.xml",
                "reports/report.xml",
                "reports/order_card.xml"
                # "views/report.xml"

            ]

}