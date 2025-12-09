"""
Base Agent - Abstract base class for all agents in the system
Defines the interface and common functionality
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """
    Abstract base class for all agents in the multi-agent system.
    
    All agents must:
    - Have a clear purpose
    - Accept specific input
    - Return structured output
    - Be stateless and isolated
    """
    
    def __init__(self, agent_id: str, agent_type: str):
        """
        Initialize the base agent.
        
        Args:
            agent_id: Unique identifier for this agent instance
            agent_type: Type/role of the agent (e.g., 'parser', 'generator')
        """
        self.agent_id = agent_id
        self.agent_type = agent_type
        self.execution_count = 0
        self.last_execution_time: Optional[datetime] = None
        
        logger.info(f"Initialized {self.agent_type} agent with ID: {self.agent_id}")
    
    @abstractmethod
    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main execution method - must be implemented by all agents.
        
        Args:
            input_data: Dictionary containing all required input for this agent
            
        Returns:
            Dictionary containing the agent's output
            
        Raises:
            ValueError: If input data is invalid
            Exception: If execution fails
        """
        pass
    
    @abstractmethod
    def validate_input(self, input_data: Dict[str, Any]) -> bool:
        """
        Validate that input data contains all required fields.
        
        Args:
            input_data: Input data to validate
            
        Returns:
            True if valid, False otherwise
        """
        pass
    
    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the agent with validation and error handling.
        
        Args:
            input_data: Input data for the agent
            
        Returns:
            Agent output with metadata
        """
        start_time = datetime.now()
        
        try:
            # Validate input
            if not self.validate_input(input_data):
                raise ValueError(f"Invalid input data for {self.agent_type} agent")
            
            logger.info(f"Starting execution of {self.agent_type} agent")
            
            # Execute main logic
            result = self.execute(input_data)
            
            # Add metadata
            execution_time = (datetime.now() - start_time).total_seconds()
            self.execution_count += 1
            self.last_execution_time = datetime.now()
            
            output = {
                'success': True,
                'data': result,
                'metadata': {
                    'agent_id': self.agent_id,
                    'agent_type': self.agent_type,
                    'execution_time': execution_time,
                    'timestamp': self.last_execution_time.isoformat(),
                    'execution_count': self.execution_count
                }
            }
            
            logger.info(
                f"{self.agent_type} agent completed in {execution_time:.2f}s"
            )
            
            return output
            
        except Exception as e:
            logger.error(f"Error in {self.agent_type} agent: {str(e)}")
            
            return {
                'success': False,
                'data': None,
                'error': str(e),
                'metadata': {
                    'agent_id': self.agent_id,
                    'agent_type': self.agent_type,
                    'timestamp': datetime.now().isoformat()
                }
            }
    
    def get_info(self) -> Dict[str, Any]:
        """
        Get information about this agent.
        
        Returns:
            Dictionary with agent information
        """
        return {
            'agent_id': self.agent_id,
            'agent_type': self.agent_type,
            'execution_count': self.execution_count,
            'last_execution_time': (
                self.last_execution_time.isoformat() 
                if self.last_execution_time else None
            )
        }
    
    def reset(self):
        """Reset agent state (execution count, etc.)"""
        self.execution_count = 0
        self.last_execution_time = None
        logger.info(f"Reset {self.agent_type} agent state")
