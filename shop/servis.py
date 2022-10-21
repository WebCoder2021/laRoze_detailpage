from .models import Orders
def set_info(order_id):
    order = Orders.objects.filter(id=order_id).first()
    text = ''
    text+='<b>Mahsulot:</b>\n'
    text+=f'<b><i>Nomi:</i></b>{order.product.name}\n'
    text+=f'<b><i>Eski narxi:</i></b>{order.product.price}\n'
    text+=f'<b><i>Chegirma:</i></b>{order.product.discount}\n'
    text+=f'<b><i>Yangi narxi:</i></b>{order.product.new_price()}\n'
    text+=f'<b><i>Qisqacha:</i></b>{order.product.content}\n\n'

    text+='<b>Buyurtmachi:</b>\n'
    text+=f'<i> <b> Rangi:</i> </b> {order.color.name}\n'
    text+=f'<i> <b> O\'lchami:</i> </b> {order.size.name}\n'
    text+=f'<i> <b> FIO:</i> </b> </b> {order.full_name}\n'
    text+=f'<i> <b>Telefon raqam:</i> </b>{order.phone_number}\n'
    text+=f'<i> <b>Manzil:</i> </b>{order.address}\n'
    text+=f'<i> <b>To\'lov shakli:</i> </b>{order.payment_type.name}\n'

    return text