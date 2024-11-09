BUDDHA_BOWL = 'buddha_bowl'
QUINOA_STIR_FRY = 'quinoa_stir_fry'
LENTIL_CURRY = 'lentil_curry'

menu = {
    "buddha_bowl": {
        "name": "buddha_bowl",
        "calories": 550,
        "price": 12.99,
        "certification": "OU",
        "ingredients": {
            "brown_rice": {
                "amount": 200,
                "unit": "g",
                "stock": 2000
            },
            "chickpeas": {
                "amount": 150,
                "unit": "g",
                "stock": 1500,
                "hechsher": "OU"
            },
            "sweet_potato": {
                "amount": 180,
                "unit": "g",
                "stock": 1800
            },
            "kale": {
                "amount": 100,
                "unit": "g",
                "stock": 1000
            },
            "tahini_sauce": {
                "amount": 30,
                "unit": "ml",
                "stock": 300,
                "hechsher": "Badatz"
            }
        },
    },
    "quinoa_stir_fry": {
        "name": "quinoa_stir_fry",
        "calories": 480,
        "price": 11.99,
        "certification": "OU",
        "ingredients": {
            "quinoa": {
                "amount": 180,
                "unit": "g",
                "stock": 1800,
                "hechsher": "OU"
            },
            "firm_tofu": {
                "amount": 150,
                "unit": "g",
                "stock": 1500,
                "hechsher": "OK"
            },
            "broccoli": {
                "amount": 120,
                "unit": "g",
                "stock": 1200
            },
            "carrots": {
                "amount": 80,
                "unit": "g",
                "stock": 800
            },
            "kosher_soy_sauce": {
                "amount": 25,
                "unit": "ml",
                "stock": 250,
                "hechsher": "OU"
            },
            "sesame_oil": {
                "amount": 15,
                "unit": "ml",
                "stock": 150,
                "hechsher": "OK"
            }
        },
    },
    "lentil_curry": {
        "name": "lentil_curry",
        "calories": 620,
        "price": 13.99,
        "certification": "OU",
        "ingredients": {
            "red_lentils": {
                "amount": 200,
                "unit": "g",
                "stock": 2000,
                "hechsher": "OU"
            },
            "kosher_coconut_milk": {
                "amount": 200,
                "unit": "ml",
                "stock": 2000,
                "hechsher": "OK"
            },
            "spinach": {
                "amount": 100,
                "unit": "g",
                "stock": 1000
            },
            "tomatoes": {
                "amount": 150,
                "unit": "g",
                "stock": 1500
            },
            "kosher_curry_paste": {
                "amount": 30,
                "unit": "g",
                "stock": 300,
                "hechsher": "Badatz"
            },
            "basmati_rice": {
                "amount": 180,
                "unit": "g",
                "stock": 1800,
                "hechsher": "OU"
            }
        },
    }
}
