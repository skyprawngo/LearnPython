add_left_menus = [
        {
            "btn_id" : "btn_home",
            "icon_file_name" : "home.svg",
            "tooltip_text" : "Home",
            "btn_istoggle" : True,
            "btn_istoggle_active" : True,
            "btn_isactive" : False
        },
        {
            "btn_id" : "btn_chart",
            "icon_file_name" : "chat-arrow-grow.svg",
            "tooltip_text" : "Chart",
            "btn_istoggle" : True,
            "btn_istoggle_active" : False,
            "btn_isactive" : False
            
        },
        {
            "btn_id" : "btn_purchased",
            "icon_file_name" : "book.svg",
            "tooltip_text" : "Purchased",
            "btn_istoggle" : True,
            "btn_istoggle_active" : False,
            "btn_isactive" : False
        },
        {
            "btn_id" : "btn_shop",
            "icon_file_name" : "shopping-cart.svg",
            "tooltip_text" : "Shop",
            "btn_istoggle" : True,
            "btn_istoggle_active" : False,
            "btn_isactive" : False
        }
    ]

print(add_left_menus[0]["btn_id"])