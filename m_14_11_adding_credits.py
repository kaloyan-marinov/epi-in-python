from typing import Dict, Set

import bintrees


class ClientsCreditsInfo:
    r_b_tree = bintrees.RBTree()
    client_id_2_credit: Dict[str, int] = {}
    # fmt: off
    '''
    def __init__(self):
        self.r_b_tree = bintrees.RBTree()
        self.client_id_2_credit: Dict[str, int] = {}
    '''
    # fmt: on

    def insert(self, client_id: str, c: int) -> None:
        # fmt: off
        '''
        if client_id in self.client_id_2_credit:
            credit = self.client_id_2_credit.pop(client_id)
            self.r_b_tree.discard((credit, client_id))
        '''
        # fmt: on

        self.r_b_tree.insert((c, client_id), None)
        self.client_id_2_credit[client_id] = c
        return

    def remove(self, client_id: str) -> bool:
        credit = self.client_id_2_credit.get(client_id)

        if credit is None:
            return False

        self.r_b_tree.discard((credit, client_id))
        # fmt: off
        del self.client_id_2_credit[client_id]
        # fmt: on
        return True

    def lookup(self, client_id: str) -> int:
        credit = self.client_id_2_credit.get(client_id)
        return credit  # `credit if credit else -1`

    def add_all(self, C: int) -> None:
        for client_id, credit in self.client_id_2_credit.items():
            self.r_b_tree.discard((credit, client_id))
            self.r_b_tree.insert(
                (credit + 1, client_id)  # >> `(credit + C, client_id), None`
            )
            self.client_id_2_credit[client_id] = credit + 1  # >> `+ C`

        return

    def max(self) -> str:
        __, client_id = self.r_b_tree.max_item()
        return client_id


class ClientsCreditsInfo2:
    def __init__(self):
        self._client_id_2_credit_amount: Dict[str, int] = {}
        self._credit_amount_2_client_ids: bintrees.RBTree[
            int, Set[str]
        ] = bintrees.RBTree()
        self._tia = 0  # total increment amount

    def insert(self, client_id: str, c: int) -> None:
        self.remove(client_id)

        self._client_id_2_credit_amount[client_id] = c - self._tia
        # fmt: off
        '''
        T.set_default(k[,d]) -> value,
        T.get(k, d), also set T[k]=d if k not in T
        '''
        # fmt: on
        self._credit_amount_2_client_ids.setdefault(c - self._tia, set()).add(
            client_id,
        )

    def remove(self, client_id: str) -> bool:
        credit_amount = self._client_id_2_credit_amount.get(client_id)

        if credit_amount is None:
            return False

        self._credit_amount_2_client_ids[credit_amount].remove(
            client_id,
        )
        if not self._credit_amount_2_client_ids[credit_amount]:
            del self._credit_amount_2_client_ids[credit_amount]

        del self._client_id_2_credit_amount[client_id]

        return True

    def lookup(self, client_id: str) -> int:
        credit_amount = self._client_id_2_credit_amount.get(client_id)
        return -1 if credit_amount is None else credit_amount + self._tia

    def add_all(self, C: int) -> None:
        self._tia += C

    def max(self) -> str:
        if not self._credit_amount_2_client_ids:
            return ""

        __, clients = self._client_id_2_credit_amount.max_item()
        return "" if not clients else next(iter(clients))
