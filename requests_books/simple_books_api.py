import requests
import random

class SimpleBooksRequests():
    #Construire url din documentatie pentru endpointul testat.
    BASE_URL = "https://simple-books-api.glitch.me"
    API_STATUS_ENDPOINT = "/status"
    GET_ALL_BOOKS_ENDPOINT = "/books"
    API_AUTH_ENDPOINT = "/api-clients"
    ORDERS_ENDPOINT = "/orders"

    ''' GET API STATUS:
    1. Construim calea catre status.
    2. Apelam Requestul de get.
    3. Returnam raspunsul.
    '''

    def get_api_status(self):
        api_status_url = self.BASE_URL + self.API_STATUS_ENDPOINT
        response = requests.get(api_status_url)
        return response

    '''Exemplu ENDPOINT afisare toate cartile cu atributele:book_type si limit:
    https://simple-books-api.glitch.me/books?type="tipcarte"&limit="limita"
    
    Construire ENDPOINT: BASE_URL + /books + ?type="" + ?limit=""
    '''

    def get_all_books(self, book_type="", limit=""):
        get_all_books_url = self.BASE_URL + self.GET_ALL_BOOKS_ENDPOINT

        if book_type != "" and limit == "":
            get_all_books_url += f"?type={book_type}"
        elif book_type == "" and limit != "":
            get_all_books_url += f"?limit={limit}"
        elif book_type != "" and limit != "":
            get_all_books_url += f"?type={book_type}&limit={limit}"

        response = requests.get(get_all_books_url)
        return response

    def generate_token(self):
        auth_url = self.BASE_URL + self.API_AUTH_ENDPOINT
        random_number = random.randint(1, 99999999999999999999)

        #DOCUMENTATIE: POST [NECESITA BODY]  - Construire EMAIL: clientName (ramane acelasi),
        # clientEmail (tmta4_client_numar@itfactory.com - unic datorita numarului de la
        # final construit cu functia random)

        request_body = {
            "clientName": "TMTA4",
            "clientEmail": f"tmta4_client_{random_number}@itfactory.com"
        }
        response = requests.post(auth_url, json=request_body)
        return response.json()['accessToken'] #valoarea cheii accessToken din rezultat

    def submit_order(self, access_token, book_id, customer_name):
        submit_order_url = self.BASE_URL + self.ORDERS_ENDPOINT
        headers_params = {"Authorization": access_token}

        #Documentatie :POST [NECESITA BODY] de tip JSON:request_body,
        # necesita autorizatie:headers_params
        request_body = {
            "bookId": book_id,
            "customerName": customer_name
        }
        response = requests.post(submit_order_url, json=request_body,headers=headers_params)
        return response

    def get_all_orders(self, access_token):
        get_all_orders_url = self.BASE_URL + self.ORDERS_ENDPOINT
        hearders_params = {"Authorization": access_token}
        response = requests.get(get_all_orders_url, headers=hearders_params)
        return response

    def get_order_byId(self, access_token, order_id):
        get_order_byId_url = self.BASE_URL + self.ORDERS_ENDPOINT + f"/{order_id}"
        hearders_params = {"Authorization": access_token}
        response = requests.get(get_order_byId_url,headers=hearders_params)
        return response

    def delete_order_byId(self, access_token, order_id):
        delete_order_byId_url = self.BASE_URL + self.ORDERS_ENDPOINT + f"/{order_id}"
        hearders_params = {"Authorization": access_token}
        response = requests.delete(delete_order_byId_url, headers=hearders_params)
        return response

    def update_order(self, access_token, order_id, new_customer_name):
        update_order_url = self.BASE_URL + self.ORDERS_ENDPOINT + f"/{order_id}"
        hearders_params = {"Authorization": access_token}


        #Documentatie: PATCH [NECESITA BODY] de tip JSON:request_body (se modifica doar nume client),
        # necesita autorizatie:headers_params si orderId (se modifica cate o carte)
        request_body={
            "customerName": new_customer_name
        }
        response = requests.patch(update_order_url, json=request_body, headers=hearders_params)
        return response









