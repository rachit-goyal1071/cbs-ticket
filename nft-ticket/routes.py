from taipy import route
from . import NftTicket

@route("/mint_nft_ticket", methods=["POST"])
def mint_nft_ticket():
    event_name = request.json["event_name"]
    date = request.json["date"]
    number_of_tickets = request.json["number_of_tickets"]
    wallet_address = request.json["wallet_address"]
    network_node_url = request.json["network_node_url"]

    nft_ticket = NftTicket(event_name, date, number_of_tickets, wallet_address, network_node_url)
    nft_ticket.mint()

    return {"nft_ticket": nft_ticket}
