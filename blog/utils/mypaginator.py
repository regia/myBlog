#!/usr/bin/env python
# -*-coding: UTF-8 -*-

from django.core.paginator import Paginator, Page


class MyPaginator(Paginator):
    def page(self, number):
        "Returns a Page object for the given 1-based page number."
        number = self.validate_number(number)
        bottom = (number - 1) * self.per_page
        top = bottom + self.per_page
        if top + self.orphans >= self.count:
            top = self.count
        return MyPage(self.object_list[bottom:top], number, self)


class MyPage(Page):
    def pages(self):
        return self.paginator.num_pages