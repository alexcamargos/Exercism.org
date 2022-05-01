def exchange_money(budget, exchange_rate):
    """
    Return the value of the exchanged currency

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    Return the amount of money that is left from the budget.

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    Return the total value of bills you now have

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """
    Return the number of bills after exchanging all your money

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return budget // denomination


def get_real_exchange_rate(exchange_rate, spread):
    """

    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :return: real exchange rate.
    """

    return exchange_rate * (1 + (spread / 100))


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Return the maximum value you can get.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    real_exchange_rate = get_real_exchange_rate(exchange_rate, spread)
    exchanged_value = exchange_money(budget, real_exchange_rate)
    bills_exchanged = get_number_of_bills(exchanged_value, denomination)

    return bills_exchanged * denomination


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Return the non-exchangeable value.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """

    real_exchange_rate = get_real_exchange_rate(exchange_rate, spread)
    number_of_bills = exchange_money(budget, real_exchange_rate)
    exchanged_value = exchangeable_value(budget, exchange_rate, spread,
                                         denomination)

    return int(number_of_bills - exchanged_value)
