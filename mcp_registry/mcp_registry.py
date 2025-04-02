"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from typing import List
from rxconfig import config

from dataclasses import dataclass


@dataclass
class MCPServer:
    """Data class representing an MCP server with its name, description and command."""

    name: str
    description: str
    command: str


class State(rx.State):
    """The app state."""

    search_query: str = ""
    servers: List[MCPServer] = [
        MCPServer(
            name="Example Server",
            description="This is an example MCP server",
            command="mcp start example",
        ),
        MCPServer(
            name="Development Server",
            description="Local development environment with hot reload",
            command="mcp start dev --hot-reload",
        ),
        MCPServer(
            name="Production Server",
            description="High-performance production server with load balancing",
            command="mcp start prod --workers 4",
        ),
        MCPServer(
            name="Testing Server",
            description="Automated testing environment with coverage reports",
            command="mcp start test --coverage",
        ),
        MCPServer(
            name="Staging Server",
            description="Pre-production environment for testing",
            command="mcp start staging --debug",
        ),
        MCPServer(
            name="Monitoring Server",
            description="Server monitoring and metrics collection",
            command="mcp start monitor --metrics",
        ),
        MCPServer(
            name="Debug Server",
            description="Development server with enhanced debugging capabilities",
            command="mcp start debug --verbose --inspect",
        ),
        MCPServer(
            name="Performance Server",
            description="Optimized server for high-throughput applications",
            command="mcp start perf --optimize --cache",
        ),
        MCPServer(
            name="Backup Server",
            description="Automated backup and recovery system",
            command="mcp start backup --interval 6h",
        ),
        MCPServer(
            name="API Server",
            description="RESTful API server with OpenAPI documentation",
            command="mcp start api --docs --port 8000",
        ),
        MCPServer(
            name="Cluster Node",
            description="Distributed computing node for scalable workloads",
            command="mcp start node --cluster main --role worker",
        ),
        MCPServer(
            name="Analytics Server",
            description="Real-time data analytics and processing server",
            command="mcp start analytics --stream --batch-size 1000",
        ),
    ]

    @rx.var
    def filtered_servers(self) -> List[MCPServer]:
        """Filter servers based on search query."""
        if not self.search_query:
            return self.servers

        query = self.search_query.lower()
        return [
            server
            for server in self.servers
            if query in server.name.lower() or query in server.description.lower()
        ]


def server_card(server: MCPServer) -> rx.Component:
    """Create a card component for an MCP server."""
    return rx.card(
        rx.vstack(
            rx.heading(
                server.name,
                size="3",
                background="linear-gradient(to right, #60A5FA, #34D399)",
                background_clip="text",
                font_weight="bold",
                margin_bottom="2",
            ),
            rx.text(
                server.description,
                color="#94A3B8",
                font_size="sm",
                margin_bottom="4",
                no_of_lines=2,
                overflow="hidden",
                text_overflow="ellipsis",
            ),
            rx.box(
                rx.hstack(
                    rx.text(
                        server.command,
                        color="#E2E8F0",
                        font_family="monospace",
                        font_size="sm",
                        overflow="hidden",
                        text_overflow="ellipsis",
                        white_space="nowrap",
                    ),
                    rx.icon(
                        "copy",
                        color="#94A3B8",
                        cursor="pointer",
                        _hover={"color": "white"},
                        on_click=rx.set_clipboard(server.command),
                    ),
                    width="100%",
                    justify="between",
                    padding="3",
                    bg="rgba(30, 41, 59, 0.5)",
                    border_radius="md",
                ),
                width="100%",
                margin_bottom="4",
            ),
            height="100%",
            spacing="0",
            align_items="start",
            width="100%",
        ),
        bg="rgba(23, 23, 23, 0.7)",
        backdrop_filter="blur(10px)",
        border_radius="xl",
        border="1px solid",
        border_color="rgba(96, 165, 250, 0.1)",
        _hover={
            "transform": "translateY(-2px)",
            "transition": "transform 0.2s ease-in-out",
            "border_color": "rgba(96, 165, 250, 0.2)",
        },
        padding="6",
        height="100%",
        variant="ghost",
    )


def index() -> rx.Component:
    """Display the MCP server registry in a grid of cards."""
    return rx.vstack(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.hstack(
                rx.heading(
                    "MCP Registry",
                    size="9",
                    color="white",
                    text_align="center",
                    font_weight="bold",
                    background="linear-gradient(to right, #FF5733, #FFC300)",
                    background_clip="text",
                ),
                rx.spacer(),
                rx.input(
                    placeholder="Search servers...",
                    value=State.search_query,
                    on_change=State.set_search_query,
                    bg="rgba(255,255,255,0.1)",
                    border="1px solid",
                    border_color="rgba(255,255,255,0.1)",
                    color="white",
                    placeholder_color="gray.400",
                    padding="2",
                    border_radius="full",
                    width="xs",
                    _focus={
                        "border_color": "rgba(255,255,255,0.2)",
                        "outline": "none",
                    },
                ),
                width="100%",
                align_items="center",
            ),
            rx.spacer(height="8"),
            rx.grid(
                rx.foreach(State.filtered_servers, server_card),
                columns="3",
                spacing="6",
                width="100%",
            ),
            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding="6",
        ),
        width="100%",
        min_height="100vh",
        bg="linear-gradient(135deg, #0f172a 0%, #1e293b 100%)",
        padding_x="8",
        padding_y="12",
    )


app = rx.App()
app.add_page(index)
