from django.db import models


class Transactions(models.Model):
    cc_num = models.CharField(blank=False, null=False, max_length=16)
    created = models.DateTimeField(auto_now_add=True)
    cvv = models.CharField(blank=False, null=False, max_length=3)
    exp_date = models.CharField(blank=False, null=False, max_length=4)
    response = models.TextField(blank=True, null=True) #See JSON example below
    response_code = models.CharField(blank=False, null=False, max_length=3)
    trans_id = models.TextField(blank=False, null=False)
    """
    # JSON Response example from Stripe
    {
        "trans_id": "ch_1HS6sv2eZvKYlo2C0OH2EYxp",
        "object": "charge",
        "amount": 100,
        "amount_refunded": 0,
        "application": null,
        "application_fee": null,
        "application_fee_amount": null,
        "balance_transaction": "txn_1032HU2eZvKYlo2CEPtcnUvl",
        "billing_details": {
            "address": {
                "city": null,
                "country": null,
                "line1": null,
                "line2": null,
                "postal_code": null,
                "state": null
            },
            "email": null,
            "name": null,
            "phone": null
        },
        "calculated_statement_descriptor": null,
        "captured": false,
        "created": 1600286745,
        "currency": "usd",
        "customer": null,
        "description": "My First Test Charge (created for API docs)",
        "disputed": false,
        "failure_code": null,
        "failure_message": null,
        "fraud_details": {},
        "invoice": null,
        "livemode": false,
        "metadata": {
            "order_id": "6735"
        },
        "on_behalf_of": null,
        "order": null,
        "outcome": null,
        "paid": true,
        "payment_intent": null,
        "payment_method": "card_1HS6ss2eZvKYlo2CO5otwLo3",
        "payment_method_details": {
            "card": {
                "brand": "visa",
                "checks": {
                    "address_line1_check": null,
                    "address_postal_code_check": null,
                    "cvc_check": "pass"
                },
                "country": "US",
                "exp_month": 8,
                "exp_year": 2021,
                "fingerprint": "Xt5EWLLDS7FJjR1c",
                "funding": "credit",
                "installments": null,
                "last4": "4242",
                "network": "visa",
                "three_d_secure": null,
                "wallet": null
            },
            "type": "card"
        },
        "receipt_email": null,
        "receipt_number": null,
        "receipt_url": "https://pay.stripe.com/receipts/acct_1032D82eZvKYlo2C/ch_1HS6sv2eZvKYlo2C0OH2EYxp/rcpt_I2BF33NcTggxhd9Amn2UX0IaN7JwG6W",
        "refunded": false,
        "refunds": {
            "object": "list",
            "data": [],
            "has_more": false,
            "url": "/v1/charges/ch_1HS6sv2eZvKYlo2C0OH2EYxp/refunds"
        },
        "review": null,
        "shipping": null,
        "source_transfer": null,
        "statement_descriptor": null,
        "statement_descriptor_suffix": null,
        "status": "succeeded",
        "transfer_data": null,
        "transfer_group": null
    }
    """

    class Meta:
        #managed = False
        db_table = 'transactions'
        verbose_name = 'transactions'
        verbose_name_plural = 'transactions'

    def save(self, *args, **kwargs):
        """
        Storing the CC Num is a breech of privacy, only keep the last 4 digits of it, replacing the first 12 as Xs
        likewise, storing the CVV is also not good, only record it as 3 Xs,
        """
        self.cc_num = str('X')*12 + self.cc_num[-4:]
        self.cvv = 'XXX'
        super(Transactions, self).save(*args, **kwargs)
