from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
import stripe


# This is a sample test API key. Sign in to see examples pre-filled with your key.
stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'


class SwipeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_data = request
        if request.method == 'POST':
            request_data = JSONParser().parse(request)

            try:
                checkout_session = stripe.checkout.Session.create({
                    "id": request_data.trans_id if request_data.trans_id else '',
                    "object": "charge",
                    "amount": request_data.amount if request_data.amount else 0,
                    #"billing_details": {
                    #    "address": {
                    #        "city": null,
                    #        "country": null,
                    #        "line1": null,
                    #        "line2": null,
                    #        "postal_code": null,
                    #        "state": null
                    #    },
                    #},
                    "currency": request_data.currency if request_data.currency else '',
                    "livemode": False, # Note: This is set here for safety, remove in production
                    #"metadata": {},
                    "payment_method_details": {
                        "card": {
                            "brand": "visa",
                            "checks": {
                                "address_line1_check": None,
                                "address_postal_code_check": None,
                                "cvc_check": "pass"
                            },
                            "country": "US",
                            "exp_month": 8,
                            "exp_year": 2021,
                            "fingerprint": "Xt5EWLLDS7FJjR1c",
                            "funding": "credit",
                            "installments": None,
                            "last4": "4242",
                            "network": "visa",
                            "three_d_secure": None,
                            "wallet": None
                        },
                        "type": "card"
                    },
                    #"source": "tok_mastercard"
                })
                response = JsonResponse(checkout_session)
            except Exception as e:
                response = JsonResponse({'error': str(e)}), 403

        response = self.get_response(request_data)
        return response

    def process_template_response(self, request, response):
        return response
