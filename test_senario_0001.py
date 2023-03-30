import requests

#TODO @fixtures
#TODO @Monkeypatch

def test_promocode_not_applied():
    url_endpoint_promo = 'https://everlywell.com/v9/promoCode'
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAAAAA1234567890'
    }

    resp = requests.get(url_endpoint_promo, headers=headers)

    assert resp.status_code != 200

def test_discount_on_purchase_of_items_subtotal():
    url_endpoint_shopping_cart = 'https://everlywell.com/v9/shoppingCart'
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAAAAA1234567890'
    }

    resp = requests.get(url_endpoint_shopping_cart, headers=headers)

    assert resp["subTotal"] == 85.0

def test_promocode_applied():
    url_endpoint_promo = 'https://everlywell.com/v9/promoCode'
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAAAAA1234567890'
    }

    resp = requests.get(url_endpoint_promo, headers=headers)

    assert resp.status_code == 200