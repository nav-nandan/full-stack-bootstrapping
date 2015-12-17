package punkboy.hack;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

@RestController
public class RequestController {

    // mapping from base path to index html page
    @RequestMapping(value = "/", method = RequestMethod.GET)
    public ModelAndView loadPage() {
        return new ModelAndView("index");
    }

    // rest service implementations go in here
    @RequestMapping("/crud")
    public @ResponseBody int crudOperations(@RequestParam(value = "id", required = true) final Integer id) {
        return id;
    }
}
