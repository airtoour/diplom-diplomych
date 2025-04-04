from .start.start import router as start

from .car.register import router as register_cars
from .solution import router as solution_router

from .social import router as social_router
from .help import router as help_router


routers_list = [
    start,
    register_cars,
    solution_router,
    social_router,
    help_router
]
