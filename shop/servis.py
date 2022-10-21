from .models import Orders
def set_info(order_id):
    order = Orders.objects.filter(id=order_id).first()
    text = ''
    text+='<b>✅ Mahsulot:</b>\n'
    text+=f'<b><i>Nomi:</i></b> {order.product.name}\n'
    text+=f'<b><i>Eski narxi:</i></b> {order.product.price}so\'m\n'
    text+=f'<b><i>Chegirma:</i></b> {order.product.discount}%\n'
    text+=f'<b><i>Yangi narxi:</i></b> {order.product.new_price()}so\'m\n'
    text+=f'<b><i>Qisqacha:</i></b> {order.product.content}\n\n'

    text+='<b>🎁 Buyurtmachi:</b>\n'
    text+=f'<b><i>Rangi:</i></b> {order.color.name}\n'
    text+=f'<b><i>O\'lchami:</i></b> {order.size.name}\n'
    text+=f'<b><i>FIO:</i></b> {order.full_name}\n'
    text+=f'<b><i>Telefon raqam:</i></b> {order.phone_number}\n'
    text+=f'<b><i>Manzil:</i> </b> {order.address}\n'
    text+=f'<b><i>To\'lov shakli:</i></b> {order.payment_type.name}\n\n'

    return text