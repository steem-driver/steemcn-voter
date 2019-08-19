# -*- coding:utf-8 -*-

from invoke import task

from steem.settings import settings
from utils.logging.logger import logger

from recipe.vote.steemcn import SteemCnVoter, SteemCnDailyVoter


class VoteCookbook:

    def __init__(self):
        self.cookbook = {}
        self._build()

    def _add(self, name, recipe):
        self.cookbook[name] = recipe

    def _get(self, name):
        return self.cookbook[name]

    def _build(self):
        self._add("steemcn", SteemCnVoter)
        self._add("steemcn_daily", SteemCnDailyVoter)

    def cook(self, recipe_name):
        recipe = self._get(recipe_name)
        recipe().run()
