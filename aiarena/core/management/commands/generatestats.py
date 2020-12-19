from django.core.management.base import BaseCommand
from django.db import transaction

from aiarena.core.models import Bot, CompetitionParticipation, Competition
from aiarena.core.stats.stats_generator import StatsGenerator


class Command(BaseCommand):
    help = "Runs the generate stats db routine to generate bot stats."


    def add_arguments(self, parser):
        parser.add_argument('--botid', type=int, help="The bot id to generate the stats for. "
                                                       "If this isn't supplied, all bots will have "
                                                       "their stats generated.")
        parser.add_argument('--competitionid', type=int, help="The competition id to generate stats for. "
                                                       "If this isn't supplied all "
                                                       "active competitions will be used")
        parser.add_argument('--allcompetitions', type=bool, help="Run this for all competition")

    def handle(self, *args, **options):
        bot_id = options['botid']
        competition = [options['competitionid'] if options['competitionid'] is not None else
                       Competition.objects.filter(status__in=['open', 'closing'])]
        if options['allcompetitions']:
            competition = Competition.objects.all()

        self.stdout.write(f'looping   {len(competition)} Competitions')
        for s in competition:
            if isinstance(s, Competition):
                competition_id = s.id
            else:
                competition_id = s
            if bot_id is not None:
                sp = CompetitionParticipation.objects.get(competition_id=competition_id, bot_id=bot_id)
                with transaction.atomic():
                    sp.lock_me()
                    self.stdout.write(f'Generating current competition stats for bot {bot_id}...')
                    StatsGenerator.update_stats(sp)
            else:
                for sp in CompetitionParticipation.objects.filter(competition_id=competition_id):
                    with transaction.atomic():
                        sp.lock_me()
                        self.stdout.write(f'Generating current competition stats for bot {sp.bot_id}...')
                        StatsGenerator.update_stats(sp)

        self.stdout.write('Done')
