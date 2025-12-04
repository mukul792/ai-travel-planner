from langchain_core.messages import HumanMessage, AIMessage
from src.chains.itinerary_chain import generate_itinerary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages = []
        self.city = ""
        self.days = 1
        self.itinerary = ""

        logger.info("Initialized TravelPlanner instance")

    def set_city(self, city: str):
        try:
            self.city = city
            self.messages.append(HumanMessage(content=f"City: {city}"))
            logger.info("City set successfully")
        except Exception as e:
            logger.error(f"Error while setting city: {e}")
            raise CustomException("Failed to set city", e)

    def set_days(self, days: int):
        try:
            self.days = days
            self.messages.append(HumanMessage(content=f"Days: {days}"))
            logger.info("Number of days set successfully")
        except Exception as e:
            logger.error(f"Error while setting days: {e}")
            raise CustomException("Failed to set days", e)

    def create_itinerary(self):
        try:
            logger.info(f"Generating itinerary for {self.city} for {self.days} days")

            itinerary = generate_itinerary(self.city, self.days)
            self.itinerary = itinerary

            self.messages.append(AIMessage(content=itinerary))

            logger.info("Itinerary generated successfully")
            return itinerary

        except Exception as e:
            logger.error(f"Error while creating itinerary: {e}")
            raise CustomException("Failed to create itinerary", e)
