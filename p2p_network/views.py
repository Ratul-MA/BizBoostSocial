from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from p2p_network.models import Transaction
from django.contrib import messages


@login_required
def make_transaction(request):
    if request.method == 'POST':
        receiver_username = request.POST.get('receiver_username')
        amount = request.POST.get('amount')
        memo = request.POST.get('memo')
        try:
            receiver = User.objects.get(username=receiver_username)
        except User.DoesNotExist:
            error_message = 'Receiver username does not exist.'
            messages.error(request, error_message)  # Add error message
            return render(request, 'p2p_network/make_transaction.html')
        sender = request.user
        Transaction.objects.create(sender=sender, receiver=receiver, amount=amount, memo=memo)
        return redirect('view_transactions')
    return render(request, 'p2p_network/make_transaction.html')

@login_required
def view_transactions(request):
    user = request.user
    sent_transactions = user.sent_transactions.all()
    received_transactions = user.received_transactions.all()
    return render(request, 'p2p_network/view_transactions.html', {'sent_transactions': sent_transactions, 'received_transactions': received_transactions})
